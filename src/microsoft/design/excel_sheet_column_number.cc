#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    int titleToNumber(string columnTitle) {
        reverse(columnTitle.begin(), columnTitle.end());
        long long res = 0;
        long long d = 1;
        for(auto c : columnTitle) {
            // cout << c << " digit: " << d << endl;
            res += d * ((long long)(c - 'A') + 1ll);
            d *= 26ll;
        }
        return res;
    }
};