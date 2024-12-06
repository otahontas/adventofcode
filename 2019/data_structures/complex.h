#ifndef _COMPLEX_H
#define _COMPLEX_H
#include <complex>

// Custom complex class inheriting from std::complex
// This class allows complex numbers to be used as keys in std::map and std::set
namespace complex {
template <typename T> class Complex : public std::complex<T> {
public:
  using std::complex<T>::complex;
  bool operator<(const Complex<T> &other) const;
};
}; // namespace complex
#endif
