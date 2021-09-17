#include <bits/stdc++.h>
using namespace std;
class Solution {

  public:
    int expressiveWords(string s, vector<string> &words) {
        vector<pair<char, int>> encoded_s = encode(s);
        vector<string> ans;
        for(auto word : words) {
            vector<pair<char, int>> encoded_word = encode(word);
            if(is_expressive(encoded_s, encoded_word)) {
                ans.push_back(word);
            }
        }
        return ans.size();
    }

    bool is_expressive(vector<pair<char, int>> target,
                       vector<pair<char, int>> word) {
        int n = target.size();
        if(n != word.size())
            return false;
        for(int i = 0; i < n; i++) {
            if(target[i].first != word[i].first)
                return false;
            if(target[i].second <= 2) {
                if(target[i].second != word[i].second)
                    return false;
            } else if(target[i].second < word[i].second)
                return false;
        }
        return true;
    }

    vector<pair<char, int>> encode(string s) {
        vector<pair<char, int>> res;
        int n = s.size();
        for(auto c : s) {
            if(res.size() == 0) {
                res.push_back({c, 1});
            } else {
                if(res[res.size() - 1].first == c) {
                    res[res.size() - 1].second++;
                } else {
                    res.push_back({c, 1});
                }
            }
        }
        return res;
    }
};