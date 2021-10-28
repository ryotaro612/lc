#include <bits/stdc++.h>
using namespace std;
class Solution {
  public:
    vector<int> partitionLabels(string s) {
        unordered_map<char, int> tail;
        int n = s.size();
        for(int i = 0; i < n; i++) {
            tail[s[i]] = i;
        }
        vector<int> res;
        for(int i = 0, from = 0, to = 0; i < n; i++) {
            if(to < tail[s[i]]) {
                to = tail[s[i]];
            } else if(to == i) {
                res.push_back(to - from + 1);
                to = from = i + 1;
            }
        }
        return res;
    }
};