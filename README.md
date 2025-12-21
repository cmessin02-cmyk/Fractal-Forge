# Fractal-Forge: A High-Performance 3D Mandelbulb Ray Marcher

Fractal-Forge is an extraordinary 3D rendering engine built to run directly in a Linux terminal. It combines the speed of **C++** with the flexibility of **Python** to visualize the infinite complexity of the Mandelbulb fractal using **ASCII Shading** and **Sphere Tracing (Ray Marching)**.

## 🚀 Why We Built This
The goal was to push the boundaries of what is possible in a "headless" terminal environment. By offloading heavy 3D trigonometric calculations to a compiled C++ core and using Python as an orchestrator, we achieve real-time 3D animation on mobile hardware (Termux/Ubuntu).

## 🧠 The Science Behind the Forge
- **Mandelbulb Logic:** Uses White and Nylander’s $n^{th}$ power formula to project the 2D Mandelbrot set into 3D space.
- **Distance Estimation:** Implements the Hubbard-Douady formula for "safe-step" sphere tracing.
- **Ray Marching:** Instead of traditional rasterization, the engine "marches" light rays to find the surface of the fractal.
- **Luminance Mapping:** Maps 3D depth data to an ASCII character set (`@#*+=-:. `) to create the illusion of lighting and shadow.

## 🛠️ Applications
While visually stunning, the logic used here applies to:
1. **Scientific Visualization:** Simulating complex mathematical topologies.
2. **Embedded Systems:** Rendering 3D data on low-power devices without GPUs.
3. **Engine Architecture:** A masterclass in C++/Python cross-language bindings via `ctypes`.

## 📦 Installation & Usage
1. **Clone the repo:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Fractal-Forge.git](https://github.com/YOUR_USERNAME/Fractal-Forge.git)
   cd Fractal-Forge
