#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;

#define REP(i,a,b) for (int i = a; i < b; i++)
#define F first
#define S second
#define PB push_back

int ans1, ans2;

vector<pair<vi,vs>> readInput() {
    string s;
    vector<pair<vi, vs>> inputs;
    while (getline(cin, s) && s.length()) {
        vi ints;
        vs strings;
        int a,b;
        stringstream ss(s);
        ss >> a >> b; ints.PB(a); ints.PB(-b);
        string t,r;
        size_t pos = s.find(":");
        t = s.substr(pos-1, 1);
        r = s.substr(pos+2);
        strings.PB(t); strings.PB(r);
        inputs.PB({ints, strings});
    }
    return inputs;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    vector<pair<vi,vs>> v = readInput();
    for (auto p : v) {
        int a = p.F[0]; int b = p.F[1];
        char c = p.S[0][0]; string r = p.S[1];
        int counter = 0;
        for (auto ch : r) {
            if (ch == c) counter++;
        }
        if (counter >= a && counter <= b) ans1++;
        if ((r[a-1] == c && r[b-1] != c) || (r[a-1] != c && r[b-1] == c)) ans2++;
    }
    cout << ans1 << "\n" << ans2 << "\n";
}
