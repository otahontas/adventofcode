#pragma once
#include <map>
#include <string>

namespace dsalgos {

    // Point struct for representing two-dimensional (x,y) points. Allows
    // - lexicographical comparison of points, so they can be used as std::map keys
    // - element-wise in-place addition of points
    struct Point {
        int x;
        int y;

        Point();
        Point(int initial_x, int initial_y); 

        Point& operator+=(const Point& rhs);
        friend bool operator==(const Point& lhs, const Point& rhs);
        friend bool operator<(const Point& lhs, const Point& rhs);
    };

    // Point for each direction, useful when moving a point to some direction.
    const std::map<std::string, Point> kDirections = {
        {"U", Point(0, -1)},
        {"R", Point(1, 0)},
        {"D", Point(0, 1)},
        {"L", Point(-1, 0)}
    };
}
