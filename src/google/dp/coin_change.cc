#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    int coinChange(vector<int> &coins, int amount) {
        vector<int> dp(amount + 1, -1);
        dp[0] = 0;
        for(int i = 1; i <= amount; i++) {
            for(auto coin : coins) {
                int base = i - coin;
                if(base >= 0 && dp[base] >= 0) {
                    if(dp[i] < 0 || dp[i] > dp[base] + 1) {
                        dp[i] = dp[base] + 1;
                    }
                }
            }
        }
        return dp[amount];
    }
};