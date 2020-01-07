#include <iostream>
#include <fstream>

using namespace std;

int main() {
    int x;
    int sum = 0;
    ifstream f("d1.txt");
    while (f >> x) {
        int s = 0;
        while (x > 6) {
            x = (x / 3) - 2;
            s += x;
        }
        sum += s;
    }
    cout << sum;
}
