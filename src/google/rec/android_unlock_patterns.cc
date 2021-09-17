#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    int numberOfPatterns(int m, int n) {
        vector<vector<int>> ans;
        vector<int> seq;
        unordered_map<int, bool> used;
        rec(m, n, seq, used, ans);
        return ans.size();
    }

    void rec(int m, int n, vector<int> &seq, unordered_map<int, bool> &used,
             vector<vector<int>> &ans) {
        if(seq.size() > n)
            return;
        if(!previous_appeared(seq, used))
            return;
        if(seq.size() >= m) {
            // vector<int> e(seq.begin(), seq.end());
            ans.push_back(seq);
        }
        for(int i = 1; i <= 9; i++) {
            if(used[i])
                continue;
            seq.push_back(i);
            used[i] = true;
            rec(m, n, seq, used, ans);
            seq.pop_back();
            used[i] = false;
        }
    }

    bool is_distinct(vector<int> &seq) {
        set<int> s(seq.begin(), seq.end());
        return s.size() == seq.size();
    }

    bool previous_appeared(vector<int> &seq, unordered_map<int, bool> &used) {
        int n = seq.size();
        if(n <= 1)
            return true;
        set<int> t = {seq[n - 1], seq[n - 2]};
        if(t.find(1) != t.end() && t.find(3) != t.end()) {
            return used[2];
        }
        if(t.find(1) != t.end() && t.find(9) != t.end()) {
            return used[5];
        }
        if(t.find(1) != t.end() && t.find(7) != t.end()) {
            return used[4];
        }
        if(t.find(2) != t.end() && t.find(8) != t.end()) {
            return used[5];
        }
        if(t.find(3) != t.end() && t.find(9) != t.end()) {
            return used[6];
        }
        if(t.find(3) != t.end() && t.find(7) != t.end()) {
            return used[5];
        }
        if(t.find(4) != t.end() && t.find(6) != t.end()) {
            return used[5];
        }
        if(t.find(7) != t.end() && t.find(9) != t.end()) {
            return used[8];
        }
        return true;
    }
};