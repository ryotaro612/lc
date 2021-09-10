#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    vector<string> findWords(vector<vector<char>> &board,
                             vector<string> &words) {
        unordered_map<char, vector<pair<int, int>>> mp;
        int h = board.size(), w = board[0].size();
        vector<vector<bool>> search(h, vector<bool>(w, false));
        for(int i = 0; i < h; i++)
            for(int j = 0; j < w; j++)
                mp[board[i][j]].push_back({i, j});
        set<string> ans;
        for(auto word : words) {
            bool ok = true;
            for(auto c : word) {
                if(mp[c].size() == 0)
                    ok = false;
            }
            if(!ok)
                continue;

            for(auto p : mp[word[0]]) {
                if(rec(p.first, p.second, h, w, word, 0, board, search))
                    ans.insert(word);
            }
        }

        return vector<string>(ans.begin(), ans.end());
    }

    bool rec(int i, int j, int h, int w, string s, int index,
             vector<vector<char>> &board, vector<vector<bool>> &search) {
        if(index == s.size())
            return true;
        if(!(i >= 0 && i < h && j >= 0 && j < w))
            return false;
        if(search[i][j])
            return false;
        search[i][j] = true;
        bool ok = false;
        if(board[i][j] == s[index]) {
            ok = rec(i - 1, j, h, w, s, index + 1, board, search) ||
                 rec(i, j + 1, h, w, s, index + 1, board, search) ||
                 rec(i + 1, j, h, w, s, index + 1, board, search) ||
                 rec(i, j - 1, h, w, s, index + 1, board, search);
        }
        search[i][j] = false;
        return ok;
    }
};
