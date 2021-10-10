#include <bits/stdc++.h>
using namespace std;
class Solution {
  public:
    int splitArray(vector<int> &nums, int m) {
        // dp[i][j]; ()
        // i番目までにj詁
        int n = nums.size();
        int inf = 1000000000;
        // sum[i] = nums[0] + ... + nums[i-1];
        vector<int> sum(n + 1, 0);
        for(int i = 1; i <= n; i++)
            sum[i] = sum[i - 1] + nums[i - 1];

        // dp[i][j] 1<=i 0<=j<=m-1 iからj番目のスロットが始まる
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, inf));
        dp[0][0] = 0;
        /*
        dp[1][1] = max(dp[0][0], sum[1]-sum[0]) 
        dp[2][1] = max(dp[0][0], sum[2]-sum[0]), max(dp[1][0], sum[2]-sum[1]);
        ..
        dp[n][1] = max(dp[0][0], sum[n]-sum[0]), max(dp[1][0], sum[n]-sum[1]);

        dp[1][2] = inf
        dp[2][2] = max(dp[1][1], sum[2]-sum[1]);
        dp[3][2] = max(dp[1][1], sum[3]-sum[1]), max(dp[2][1], sum[3]-sum[2]);
        ..
        dp[n][2] = max(dp[1][1], sum[n]-sum[1]), max(dp[2][1], sum[n]-sum[2]), max(dp[3][1], sum[n]-sum[3]),..max(dp[n-1][1], sum[n] - sum[n-1]);

        dp[1][3] = inf
        dp[2][3] = inf
        dp[3][3] = max(dp[2][2], sum[3]-sum[2]);
        dp[4][3] = max(dp[2][2], sum[4]-sum[2]), max(dp[3][2], sum[4]-sum[3]);
        dp[5][3] = max(dp[2][2], sum[5]-sum[2]), max(dp[3][2], sum[5]-sum[3]), max(dp[4][2], sum[5]-sum[4]);

        dp[i][j] = max(dp[j-1][j-1], sum[i]-sum[j-1]), max(dp[j][j-1], sum[i]-sum[j]), max(dp[j+1][j-1], sum[i]-sum[j+1]);
        ... max(dp[i-1][j-1], sum[i]-sum[i-1]);
        */
        for(int j = 1; j <= m; j++) {
            for(int i = 1; i <= n; i++) {
                for(int k = j;k <= i;k++) {
                    int candidate = max(dp[k-1][j-1], sum[i]-sum[k-1]);
                    dp[i][j] = min(candidate, dp[i][j]);
                }
            }
        }

        return dp[n][m];
    }
};
/*
class Solution {
  public:
    int splitArray(vector<int> &nums, int m) {
        // dp[i][j]; ()
        // i番目までにj詁
        int n = nums.size();
        int inf = 1000000000;
        // sum[i] = nums[0] + ... + nums[i-1];
        vector<int> sum(n + 1, 0);
        for(int i = 1; i <= n; i++)
            sum[i] = sum[i - 1] + nums[i - 1];
        if(m == 1)
            return sum[n];
        // dp[i][j] 1<=i 0<=j<=m-1 iからj番目のスロットが始まる
        vector<vector<int>> dp(n + 1, vector<int>(m, inf));
        dp[0][0] = 0;

        for(int i = 1; i <= n; i++) {
            for(int j = 0; j < min(i, m); j++) {
                if(j == 0) {
                    dp[i][j] = sum[i];
                } else {
                    for(int k = 0; k < i; k++) {
                        int temp = max(dp[k][j - 1], sum[i] - sum[k]);
                        dp[i][j] = min(dp[i][j], temp);
                    }
                }
            }
        }
        int res = inf;
        for(int i = 1; i <= n; i++) {
            // dp[i][m-1] -> nums[i-1] + .. + nums[n-1]
            int candidate = max(dp[i][m - 1], sum[n] - sum[i - 1]);
            res = min(res, candidate);
        }
        return res;
    }
};
*/