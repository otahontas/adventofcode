#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

typedef vector<string> vs;

#define REP(i,a,b) for (int i = a; i < b; i++)
#define PB push_back
#define F first
#define S second

int n;
vs inputs;

void readInput() {
    string s;
    while (getline(cin, s) && s.length()) inputs.PB(s);
    n = inputs.size();
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    readInput();
    int twice = 0;
    int trice = 0;
    vector<pair<string,int>> sorted_inputs;
    REP(i,0,n) {
        string s = inputs[i];
        char chars[128] = { 0 };
        for (auto ch : s) chars[(int) ch]++;
        bool found_twice = false;
        bool found_trice = false;
        REP(j,0,128) {
            if (!found_twice && chars[j] == 2) {
                twice++;
                found_twice = true;
            }
            if (!found_trice && chars[j] == 3) {
                trice++;
                found_trice = true;
            }
        }
        string t = s;
        sort(t.begin(), t.end());
        sorted_inputs.PB({t, i});
    }
    cout << twice * trice << "\n";
    sort(sorted_inputs.begin(), sorted_inputs.end());

    string ans;
    REP(i,1,n) {
        int diffs = 0;
        string s = sorted_inputs[i].F;
        string t = sorted_inputs[i-1].F;
        REP(j,0,(int) s.size()) {
            if (s[j] != t[j]) diffs++;
        }
        if (diffs == 1) {
            s = inputs[sorted_inputs[i].S];
            t = inputs[sorted_inputs[i-1].S];
            REP(j,0,(int) s.size()) {
                if (s[j] == t[j]) ans += s[j];
            }
        }
    }
    cout << ans << "\n";
}
