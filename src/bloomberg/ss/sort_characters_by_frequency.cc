#include <bits/stdc++.h>
using namespace std;
/*
"tree"
"cccaaa"
"Aabb"
*/
class Solution {
  public:
    string frequencySort(string s) {
        unordered_map<char, int> freq;
        for(auto c : s)
            freq[c]++;
        vector<pair<int, char>> v;
        for(auto e : freq) {
            v.push_back({e.second, e.first});
        }
        sort(v.begin(), v.end(), greater<pair<int, char>>());
        string res;
        for(auto e : v) {
            for(int i = 0; i < e.first; i++) {

                res.push_back(e.second);
            }
        }
        return res;
    }
};