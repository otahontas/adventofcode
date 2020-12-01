#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;
typedef vector<ll> vll;
//typedef vector<ll> vll;
//typedef pair<int, int> pi;
//typedef vector<pi> vpi;

#define REP(i,a,b) for (int i = a; i < b; i++)
#define RREP(i,a,b) for (int i = a; i <= b; i++)
#define F first
#define S second
#define PB push_back

int n;
vll v;

bool are_same(float a, float b) {
    if (abs(a-b) < 1e-9) return true;
    return false;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    ll x;
    while (cin >> x) {
        v.PB(x);
    }
    n = v.size();
    cout << n << "\n";
    REP(i,0,n) {
        cout << v[i] << " ";
    }
    cout << "\n";
}
