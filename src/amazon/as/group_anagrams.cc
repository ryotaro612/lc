#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    vector<vector<string>> groupAnagrams(vector<string> &strs) {
        int n = strs.size();
        unordered_map<string, vector<string>> mp;
        for(int i = 0; i < n; i++) {
            string s = string(strs[i]);
            sort(strs[i].begin(), strs[i].end());
            mp[strs[i]].push_back(s);
        }
        vector<vector<string>> res;
        for(auto e : mp)
            res.push_back(e.second);
        return res;
    }
};