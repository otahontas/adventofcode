#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <string>

using namespace std;

typedef long long ll;
typedef vector<string> vs;
typedef vector<int> vi;

#define REP(i,a,b) for (int i = a; i < b; i++)
#define DREP(i,a,b) for (int i = a; i < b; i+=2)
#define PB push_back

int n;
ll ans1;
ll ans2;
vs inputs;

void readInput() {
    string s;
    while (getline(cin, s) && s.length()) inputs.PB(s);
    n = inputs.size();
}

int travel(int add_x, int add_y) {
    int x = 0; int y = 0; ll counter = 0;
    int width = inputs[y].size();
    while (true) { 
        x += add_x; y += add_y;
        if (y >= n) break;
        if (x >= width) x %= width;
        if (inputs[y][x] == '#') counter++;
    }
    return counter;
}


int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    readInput();
    ans1 = travel(3, 1);
    ans2 = ans1;
    vi v{1,1,5,1,7,1,1,2};
    DREP(i,0,(int) v.size()) ans2 *= travel(v[i], v[i+1]);
    cout << ans1 << "\n" << ans2 << "\n";
}
