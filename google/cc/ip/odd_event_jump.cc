#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

class Solution {
  public:
    int oddEvenJumps(vector<int> &arr) {
        int n = arr.size();
        vector<vector<bool>> dp(n, vector<bool>(2, false));
        vector<int> idx(100000, 0);
        dp[n - 1][0] = dp[n - 1][1] = true;
        set<int> sorted;
        sorted.insert(arr[n - 1]);
        idx[arr[n - 1]] = n - 1;
        for(int i = n - 2; i >= 0; i--) {
            auto iter = sorted.lower_bound(arr[i]);

            if(iter != sorted.end()) {
                dp[i][0] = dp[idx[*iter]][1];
                if(arr[i] == *iter) {
                    dp[i][1] = dp[idx[*iter]][0];
                } else if(iter != sorted.begin()) {
                    dp[i][1] = dp[idx[*(--iter)]][0];
                    iter++;
                }
            } else {
                dp[i][1] = dp[idx[*(--iter)]][0];
                iter++;
            }
            sorted.insert(arr[i]);
            idx[arr[i]] = i;
        }

        int ans = 0;
        for(int i = 0; i < (int)arr.size(); i++)
            if(dp[i][0])
                ans++;
        return ans;
    }
};