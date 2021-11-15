#include <bits/stdc++.h>
using namespace std;
/*
"leetcode"
["leet","code"]
"applepenapple"
["apple","pen"]
"catsandog"
["cats","dog","sand","and","cat"]
*/
class Solution {
  public:
    bool wordBreak(string s, vector<string> &wordDict) {
        vector<bool> dp(s.size() + 1, false);
        dp[0] = true;
        int n = s.size();
        for(int i = 1; i <= n; i++) {
            if(dp[i - 1]) {
                for(auto word : wordDict) {
                    int remain = n - (i - 1); // remaining string length;
                    if((int)word.size() <= remain) {
                        auto from = s.begin() + i - 1;
                        auto to = from + word.size();
                        if(word == string(s.begin() + i - 1, to)) {
                            dp[i - 1 + word.size()] = true;
                        }
                    }
                }
            }
        }
        return dp[s.size()];
    }
};