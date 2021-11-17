#include <bits/stdc++.h>
using namespace std;
class Solution {
  public:
    vector<vector<int>> candyCrush(vector<vector<int>> &board) {
        int n = board.size(), m = board[0].size();
        while(true) {
            bool halt = true;
            vector<vector<bool>> keep(n, vector<bool>(m, true));
            for(int i = 0; i < n; i++) {
                for(int j = 0; j < m; j++) {
                    if(board[i][j] == 0)
                        continue;
                    if(0 < i && i < n - 1 && board[i - 1][j] == board[i][j] &&
                       board[i][j] == board[i + 1][j]) {
                        keep[i - 1][j] = keep[i][j] = keep[i + 1][j] = false;
                        halt = false;
                    }
                    if(0 < j && j < m - 1 && board[i][j - 1] == board[i][j] &&
                       board[i][j] == board[i][j + 1]) {
                        keep[i][j - 1] = keep[i][j] = keep[i][j + 1] = false;
                        halt = false;
                    }
                }
            }
            // debug_keep(keep);
            if(halt)
                break;
            for(int j = 0; j < m; j++) {
                deque<int> que;
                for(int i = n - 1; i >= 0; i--) {
                    if(keep[i][j]) {
                        que.push_front(board[i][j]);
                    }
                }
                for(int i = n - 1; i >= 0; i--) {
                    if(que.empty()) {
                        board[i][j] = 0;
                    } else {
                        board[i][j] = que.back();
                        que.pop_back();
                    }
                }
            }
            // cout << "--" << endl;
            // debug_board(board);
            // cout << " --- " << endl;
        }
        return board;
    }
    void debug_keep(vector<vector<bool>> &keep) {
        for(auto line : keep) {
            for(auto e : line) {
                cout << e << " ";
            }
            cout << endl;
        }
    }
    void debug_board(vector<vector<int>> &board) {
        for(auto line : board) {
            for(auto e : line) {
                printf("%04d ", e);
            }
            cout << endl;
        }
    }
};