#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    int maxProfit(vector<int> &prices) {
        int n = prices.size();
        vector<int> mini(n, 10001);
        for(int i = 1; i < n; i++)
            mini[i] = min(mini[i - 1], prices[i - 1]);
        int ans = 0;
        for(int i = 1; i < n; i++)
            ans = max(ans, prices[i] - mini[i]);
        return ans;
    }
};