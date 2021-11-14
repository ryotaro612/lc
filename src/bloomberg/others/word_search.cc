#include <bits/stdc++.h>
using namespace std;
/*
[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
"ABCCED"
 [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
"SEE"
[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
"ABCB"
[["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]]
"AAAAAAAAAAAABAA"
*/
class Solution {
  public:
    bool exist(vector<vector<char>> &board, string word) {
        unordered_set<char> b_set;
        for(auto row : board) {
            for(auto c : row)
                b_set.insert(c);
        }
        for(auto c : word) {
            if(b_set.find(c) == b_set.end())
                return false;
        }
        int m = board.size();
        int n = board[0].size();
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(rec(0, i, j, word, board))
                    return true;
            }
        }
        return false;
    }
    bool rec(int word_index, int i, int j, string &word,
             vector<vector<char>> &board) {
        if(word_index == (int)word.size())
            return true;
        int m = board.size(), n = board[0].size();
        if(!(0 <= i && i < m && 0 <= j && j < n) ||
           word[word_index] != board[i][j]) {
            return false;
        }

        board[i][j] = '#';
        vector<pair<int, int>> deltas = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
        for(auto delta : deltas) {
            int y = i + delta.first;
            int x = j + delta.second;
            if(rec(word_index + 1, y, x, word, board)) {
                board[i][j] = word[word_index];
                return true;
            }
        }
        board[i][j] = word[word_index];
        return false;
    }
};