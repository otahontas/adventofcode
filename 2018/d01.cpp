#include <iostream>
#include <vector>
#include <set>

using namespace std;

typedef vector<int> vi;
typedef set<int> si;

#define PB push_back

int ans1, ans2, x,n;
si s;
vi v;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    while (cin >> x) {
        v.PB(x);
        ans1 += x;
    }
    n = v.size();
    int sum = 0; int i = 0;
    while (true) {
        sum += v[i];
        if (s.count(sum) && !ans2) {
            ans2 = sum;
            break;
        }
        s.insert(sum);
        i++;
        i %= n;
    }
    cout << ans1 << "\n" << ans2 << "\n";
}
