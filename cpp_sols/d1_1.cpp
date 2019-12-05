#include <iostream>
#include <fstream>

using namespace std;

int main() {
    int x;
    int sum = 0;
    ifstream f("d1.txt");
    while (f >> x) {
        sum += (x / 3) - 2;
    }
    cout << sum;
}
