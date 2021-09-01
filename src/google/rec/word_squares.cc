#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    vector<vector<string>> wordSquares(vector<string> &words) {
        int size = words[0].size();
        vector<vector<string>> ans;
        for(auto word : words) {
            vector<unordered_set<string>> cands(size);
            bool ok = true;
            for(int i = 1; i < size; i++) {
                // cout << word << " " << i << endl;
                for(string cand : words) {
                    if(word[i] == cand[0]) {
                        // cout << i << " " << cand << endl;
                        cands[i].insert(cand);
                    }
                }
                if(cands[i].empty()) {
                    ok = false;
                    break;
                }
            }
            if(ok) {
                vector<string> s = {word};
                rec(1, size, s, cands, ans);
            }
        }
        return ans;
    }

    void rec(int index, int size, vector<string> s,
             vector<unordered_set<string>> cands, vector<vector<string>> &ans) {
        if(index == size) {
            if((int)s.size() == size)
                ans.push_back(s);
            return;
        }
        for(string word : cands[index]) {
            vector<unordered_set<string>> next_cands(size);
            vector<string> next_s(s);
            bool ok = true;
            for(int i = index + 1; i < size; i++) {
                for(auto cand : cands[i]) {
                    if(word[i] == cand[index]) {
                        next_cands[i].insert(cand);
                    }
                }
                if(next_cands[i].empty()) {
                    ok = false;
                    break;
                }
            }
            next_s.push_back(word);

            if(ok) {
                rec(index + 1, size, next_s, next_cands, ans);
            }
        }
    }
};