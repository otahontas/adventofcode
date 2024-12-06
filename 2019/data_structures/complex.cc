#include "complex.h"
#include <complex>

namespace complex {
template <typename T>
bool Complex<T>::operator<(const Complex<T> &other) const {
  return (this->real() < other.real()) ||
         (this->real() == other.real() && this->imag() < other.imag());
}

// Explicit instantiations
template class Complex<int>;
} // namespace complex
