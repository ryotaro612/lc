#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    string longestPalindrome(string s) {
        int n = s.size();
        vector<vector<int>> dp(n, vector<int>(n + 1, 0));
        int a_len = 1, head = 0;

        for(int len = 1; len <= n; len++) {
            for(int from = 0; from + len <= n; from++) {
                int to = from + len;
                if(to - from == 1) {
                    dp[from][to] = 1;
                } else {
                    if(s[from] == s[to - 1] &&
                       dp[from + 1][to - 1] == to - 1 - (from + 1)) {
                        dp[from][to] = dp[from + 1][to - 1] + 2;
                    }
                }
                if(to - from == dp[from][to] && a_len < to - from) {
                    a_len = to - from;
                    head = from;
                }
            }
        }
        return s.substr(head, a_len);
    }
};