#ifndef MATH_UTILS_H
#define MATH_UTILS_H

#include <cmath>

struct Vec3 {
    float x, y, z;

    // Basic Vector addition
    Vec3 operator+(const Vec3& v) const { return {x + v.x, y + v.y, z + v.z}; }
    
    // Basic Vector subtraction
    Vec3 operator-(const Vec3& v) const { return {x - v.x, y - v.y, z - v.z}; }

    // Scalar multiplication (scaling the ray)
    Vec3 operator*(float f) const { return {x * f, y * f, z * f}; }

    // Magnitude (Length) of the vector
    float length() const { return std::sqrt(x * x + y * y + z * z); }

    // Normalize (make the vector length 1.0)
    Vec3 normalize() const {
        float l = length();
        return {x / l, y / l, z / l};
    }
};

#endif
