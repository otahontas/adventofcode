#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;
typedef vector<ll> vll;

#define REP(i,a,b) for (int i = a; i < b; i++)
#define PB push_back

int n;
vll v;

bool are_same(float a, float b) {
    if (abs(a-b) < 1e-9) return true;
    return false;
}

void solve() {
    ll goal = 2020;
    REP(i,0,n-1) {
        REP(j,i,n) {
            if (v[i]+v[j] == goal) {
                cout << v[i] * v[j] << "\n";
                return;
            }
        }
    }
}


void solve2() {
    ll goal = 2020;
    REP(i,0,n-2) {
        REP(j,i,n-1) {
            REP(k,j,n) {
                if (v[i]+v[j]+v[k] == goal) {
                    cout << v[i] * v[j] * v[k] << "\n";
                    return;
                }
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    ll x;
    while (cin >> x) {
        v.PB(x);
    }
    n = v.size();
    solve();
    solve2();
}
