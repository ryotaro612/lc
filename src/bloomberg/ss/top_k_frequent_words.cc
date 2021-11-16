#include <bits/stdc++.h>
using namespace std;
/*
["i","love","leetcode","i","love","coding"]
2
["the","day","is","sunny","the","the","the","sunny","is","is"]
4
*/
class Solution {
  public:
    vector<string> topKFrequent(vector<string> &words, int k) {
        unordered_map<string, int> freq;
        for(auto word : words)
            freq[word]++;
        vector<pair<int, string>> freq_vec;
        for(auto e : freq)
            freq_vec.push_back({e.second, e.first});
        sort(freq_vec.begin(), freq_vec.end(),
             [](const pair<int, string> &l, const pair<int, string> &r) {
                 if(l.first != r.first)
                     return r.first < l.first;
                 return l.second < r.second;
             });
        vector<string> res;
        for(int i = 0; i < k; i++)
            res.push_back(freq_vec[i].second);
        return res;
    }
};