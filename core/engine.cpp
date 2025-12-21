#include "math_utils.hpp"
#include <algorithm>
#include <cmath>

extern "C" {

    // 1. Distance Estimator (DE)
    // This function defines the shape of the Mandelbulb
    float get_distance(float px, float py, float pz) {
        Vec3 pos = {px, py, pz};
        Vec3 z = pos;
        float dr = 1.0;
        float r = 0.0;
        int iterations = 8;
        float power = 8.0;

        for (int i = 0; i < iterations; i++) {
            r = z.length();
            if (r > 2.0) break; // Bailout

            // Convert to Spherical Coordinates
            float theta = std::acos(z.z / r);
            float phi = std::atan2(z.y, z.x);
            
            // Derivative for distance estimation
            dr = std::pow(r, power - 1.0) * power * dr + 1.0;

            // Scale and rotate
            float zr = std::pow(r, power);
            theta *= power;
            phi *= power;

            // Convert back to Cartesian
            z.x = zr * std::sin(theta) * std::cos(phi);
            z.y = zr * std::sin(theta) * std::sin(phi);
            z.z = zr * std::cos(theta);
            
            z = z + pos;
        }
        return 0.5 * std::log(r) * r / dr;
    }

    // 2. Ray Marching Engine
    // This function shoots a ray and finds the surface
    float march(float roX, float roY, float roZ, float rdX, float rdY, float rdZ) {
        float total_dist = 0.0;
        int max_steps = 128;
        float hit_threshold = 0.001;
        float max_view_dist = 10.0;

        Vec3 ro = {roX, roY, roZ}; // Camera Position
        Vec3 rd = {rdX, rdY, rdZ}; // Ray Direction

        for (int i = 0; i < max_steps; i++) {
            Vec3 p = ro + rd * total_dist;
            float d = get_distance(p.x, p.y, p.z);
            
            if (d < hit_threshold) return total_dist; // HIT!
            
            total_dist += d;
            if (total_dist > max_view_dist) break; // MISS
        }
        return -1.0;
    }

    // 3. Test Function (Handshake)
    float test_vector_logic(float x, float y, float z) {
        Vec3 v = {x, y, z};
        return v.length();
    }
}
