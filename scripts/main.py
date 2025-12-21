import os
import time
import math
from bridge import get_engine

# ASCII characters from brightest (hit) to darkest (far)
CHARS = "@#*+=-:. "

def render_animated():
    eng = get_engine()
    
    t = 0.0  # Time/Rotation variable
    
    try:
        while True:
            # 1. Get current terminal size
            cols, rows = os.get_terminal_size()
            
            # 2. Camera Orbit Math
            radius = 3.0
            ro_x = radius * math.sin(t)
            ro_z = radius * math.cos(t)
            ro_y = 1.0 * math.sin(t * 0.5) # Gentle up/down bobbing
            
            # 3. Calculate "Look At" Direction (pointing to 0,0,0)
            # This logic mimics a real 3D camera matrix
            forward_x, forward_y, forward_z = -ro_x, -ro_y, -ro_z
            # Normalize forward vector
            f_len = math.sqrt(forward_x**2 + forward_y**2 + forward_z**2)
            fx, fy, fz = forward_x/f_len, forward_y/f_len, forward_z/f_len
            
            # Right vector (perpendicular to forward and up)
            rx, ry, rz = fz, 0, -fx 
            r_len = math.sqrt(rx**2 + rz**2)
            rx, rz = rx/r_len, rz/r_len
            
            # Up vector
            ux, uy, uz = (fy*rz - fz*ry), (fz*rx - fx*rz), (fx*ry - fy*rx)

            frame = []
            for y in range(rows):
                line = ""
                for x in range(cols):
                    # Normalize screen coordinates
                    uv_x = (x / cols) * 2.0 - 1.0
                    uv_y = (y / rows) * 2.0 - 1.0
                    uv_x *= (cols / rows) * 0.5 # Aspect ratio correction
                    
                    # Calculate Ray Direction based on Camera Matrix
                    rd_x = fx + uv_x * rx + uv_y * ux
                    rd_y = fy + uv_x * ry + uv_y * uy
                    rd_z = fz + uv_x * rz + uv_y * uz
                    
                    # Normalize rd
                    rd_len = math.sqrt(rd_x**2 + rd_y**2 + rd_z**2)
                    rd_x, rd_y, rd_z = rd_x/rd_len, rd_y/rd_len, rd_z/rd_len

                    # 4. Call C++ Engine
                    dist = eng.march(ro_x, ro_y, ro_z, rd_x, rd_y, rd_z)
                    
                    if dist > 0:
                        # Shading based on distance
                        idx = int((dist / 5.0) * len(CHARS))
                        idx = max(0, min(len(CHARS) - 1, idx))
                        line += CHARS[idx]
                    else:
                        line += " "
                frame.append(line)
            
            # 5. Print frame (ANSI escape H moves cursor to top-left)
            print("\033[H" + "\n".join(frame), end="", flush=True)
            
            t += 0.1  # Speed of rotation
            time.sleep(0.01) # Small delay to save CPU
            
    except KeyboardInterrupt:
        print("\nAnimation Stopped.")

if __name__ == "__main__":
    # Clear screen once
    print("\033[2J")
    render_animated()
