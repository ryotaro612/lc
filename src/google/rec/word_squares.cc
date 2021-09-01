#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    vector<vector<string>> wordSquares(vector<string> &words) {
        int size = words[0].size();
        vector<vector<string>> ans;
        vector<unordered_set<string>> cands(size + 1);
        for(auto word : words) {
            for(int i = 1; i < size; i++) {
                for(string cand : words) {
                    if(word[i] == cand[i]) {
                        cands[i].insert(cand);
                    }
                }
            }

            vector<string> s = {word};
            rec(1, size, s, cands, ans);
        }
        return ans;
    }

    void rec(int index, int size, vector<string> s,
             vector<unordered_set<string>> cands, vector<vector<string>> &ans) {
        if(index == size) {
            ans.push_back(s);
            return;
        }
        vector<unordered_set<string>> next_cands(size);
        for(string word : cands[index]) {
            for(int i = index + 1; i < size; i++) {
                for(auto cand : cands[i]) {
                    if(word[i] == cand[i]) {
                        next_cands[i].insert(cand);
                    }
                }
            }
            s.push_back(word);
            rec(index+1, size, s, next_cands, ans);
        }
    }
};