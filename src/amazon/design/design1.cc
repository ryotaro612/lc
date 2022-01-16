#include <bits/stdc++.h>
using namespace std;
class TicTacToe {
public:
    TicTacToe(int n): n(n) {
        winner = 0;
        rows = vector<vector<int>>(2, vector<int>(n, 0));
        cols = vector<vector<int>>(2, vector<int>(n, 0));
        diags = vector<int>(2, 0);
        rev_diags = vector<int>(2, 0);
    }
    
    int move(int row, int col, int player) {
        player--;
        if(winner)
            return winner;
        rows[player][row]++;
        cols[player][col]++;
        if(row == col) {
            diags[player]++;
        }
        if(col == n-1 - row) {
            rev_diags[player]++;
        }
        /*
        cout << player + 1 << endl;
        cout << " row ";
        for(int i = 0;i<n;i++) {
            cout << rows[player][i] << " ";
        }
        cout << endl;
        cout << " col ";
        for(int i = 0;i<n;i++) {
            cout << cols[player][i] << " ";
        }
        cout << endl;
        */
        if(diags[player] == n || rev_diags[player] == n) {
            winner = player + 1;
            return winner;
        }
        int mx = max(*max_element(rows[player].begin(), rows[player].end()), 
                     *max_element(cols[player].begin(), cols[player].end()));
        if(mx == n) {
            winner = player + 1;
            return winner;
        }
        return 0;
    }
private:
    int winner, n;
    vector<vector<int>> rows, cols;
    vector<int> diags, rev_diags;
};

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe* obj = new TicTacToe(n);
 * int param_1 = obj->move(row,col,player);
 */
