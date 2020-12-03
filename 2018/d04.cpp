#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <string>
#include <set>
#include <map>

using namespace std;

typedef long long ll;
typedef pair<int, int> pi;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<ll> vll;
typedef vector<pi> vpi;
typedef set<int> si;

#define REP(i,a,b) for (int i = a; i < b; i++)
#define DREP(i,a,b) for (int i = a; i < b; i+=2)
#define RREP(i,a,b) for (int i = a; i <= b; i++)
#define F first
#define S second
#define PB push_back

int n;
int ans1, ans2;
map<int, vi> amounts;
vs inputs;

void readInput() {
    string s;
    while (getline(cin, s) && s.length()) inputs.PB(s);
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    readInput();
    sort(inputs.begin(), inputs.end());
    int id = 0;
    int start = 0;
    for (auto s : inputs) {
        string info = s.substr(19);
        if (info[0] == 'G') {
            id = stoi(info.substr(7,5));
            if (amounts[id].size() == 0) amounts[id].resize(60);
        } else {
            int time = stoi(s.substr(15,2));
            if (info[0] == 'f') {
                start = time;
            } else {
                REP(i,start,time) amounts[id][i]++;
            }
        } 
    }
    int most_frequent_minute_amount = 0;
    int most_frequent_id = 0;
    int most_frequent_minute = 0;
    int highest_sum = 0;
    int highest_id = 0;
    int highest_minute = 0;
    auto it = amounts.begin();
    while (it != amounts.end()) {
        int sum = 0;
        int highest_minute_for_this = 0;
        int highest_minute_amount_for_this = 0;
        int most_frequent_minute_for_this = 0;
        int most_frequent_minute_amount_for_this = 0;
        REP(i,0,60) {
            int times = it->second[i];
            sum += times;
            if (times > highest_minute_amount_for_this) {
                highest_minute_for_this = i;
                highest_minute_amount_for_this = times;
            }
            if (times > most_frequent_minute_amount_for_this) {
                most_frequent_minute_for_this = i;
                most_frequent_minute_amount_for_this = times;
            }
        }
        if (sum > highest_sum) {
            highest_sum = sum;
            highest_id = it->first;
            highest_minute = highest_minute_for_this;
        }
        if (most_frequent_minute_amount_for_this > most_frequent_minute_amount) {
            most_frequent_minute_amount = most_frequent_minute_amount_for_this;
            most_frequent_id = it->first;
            most_frequent_minute = most_frequent_minute_for_this;
            cout << "id: " << most_frequent_id << " + stats: ";
            cout << most_frequent_minute << ", " << most_frequent_minute_amount << "\n";
        }
        it++;
    }
    cout << highest_id * highest_minute << "\n";
    cout << most_frequent_id * most_frequent_minute << "\n";
}
