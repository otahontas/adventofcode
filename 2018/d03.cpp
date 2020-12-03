#include <iostream>
#include <vector>
#include <sstream>
#include <map>

using namespace std;

typedef pair<int, int> pi;
typedef vector<int> vi;

#define REP(i,a,b) for (int i = a; i < b; i++)
#define PB push_back

int n;

map<pi, int> covered;
vector<vi> inputs;

void readInput() {
    string s;
    int id = 1;
    while (getline(cin, s) && s.length()) {
        size_t del = s.find("@");
        string t = s.substr(del+1); 
        stringstream ss(t);
        vi ints;
        int i;
        while (ss >> i) {
            ints.PB(i);
            if (ss.peek() == ',' || ss.peek() == 'x' || ss.peek() == ':') ss.ignore();
        }
        ints.PB(id);
        id++;
        inputs.PB(ints);
    }
    n = inputs.size();
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    readInput();
    for (auto ints : inputs){
        int x = ints[0]; int y = ints[1]; int w = ints[2]; int h = ints[3];
        REP(i,y,y+h) {
            REP(j,x,x+w) {
                covered[{i,j}]++;
            }
        }
    }
    int ans1 = 0;
    int ans2 = 0;
    auto it = covered.begin();
    while (it != covered.end()) {
        if (it->second > 1) ans1++;
        it++;
    }
    for (auto ints : inputs){
        int x = ints[0]; int y = ints[1]; int w = ints[2]; int h = ints[3]; int id = ints[4];
        bool overlapping = false;
        REP(i,y,y+h) {
            if (overlapping) break;
            REP(j,x,x+w) {
                if (covered[{i,j}] != 1) overlapping = true;
            }
        }
        if (!overlapping) ans2 = id;
    }
    cout << ans1 << "\n" << ans2 << "\n";
}
