#include <iostream>
#include <fstream>
#include <vector>
#define REP(i,a,b) for (int i = a; i < b; i++)

using namespace std;

int main() {
    int x,i = 0;
    vector<int> v;
    ifstream f("day3_input.txt");
    while (f >> x) {
        v.push_back(x);
        if (f.peek() == ',')
            f.ignore();
    }

    while (v[i] != 99) {
        if (v[i] == 1) {
            v[v[i+3]] = v[v[i+1]] + v[v[i+2]];
        } else {
            v[v[i+3]] = v[v[i+1]] * v[v[i+2]];
        }
        i+=4;
    }
    cout << v[0];
}
