#include "dsalgos.h"

namespace dsalgos {

    Point::Point() {
        x = 0;
        y = 0;
    }

    Point::Point(int initial_x, int initial_y) {
        x = initial_x;
        y = initial_y;
    }
    
    Point& Point::operator+=(const Point& rhs) {
        this->x += rhs.x;
        this->y += rhs.y;
        return *this;
    };

    bool operator==(const Point& lhs, const Point& rhs) {
        return (lhs.x == rhs.x) && (lhs.y == rhs.y);
    }
    bool operator<(const Point& lhs, const Point& rhs) {
        return (lhs.x < rhs.x) || ((lhs.x == rhs.x) && (lhs.y < rhs.y));
    }

}
