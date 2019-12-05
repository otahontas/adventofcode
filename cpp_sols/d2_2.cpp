#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
    int x;
    vector<int> v;
    ifstream f("d2_input.txt");
    while (f >> x) {
        v.push_back(x);
        if (f.peek() == ',')
            f.ignore();
    }
    for (int i = 0; i < 100; i++) {
        for (int j = 0; j < 100; j++) {
            vector<int> t(v);
            t[1]=i;
            t[2]=j;
            int k = 0;
            while (t[k] != 99) {
                if (t[k] == 1) {
                    t[t[k+3]] = t[v[k+1]] + t[t[k+2]];
                } else {
                    t[t[k+3]] = t[t[k+1]] * t[t[k+2]];
                }
                k+=4;
            }
            if (t[0] == 19690720) {
                cout << "solution found, so 100 * noun + verb = " << 100 * i + j;
            }
        }
    }
}
