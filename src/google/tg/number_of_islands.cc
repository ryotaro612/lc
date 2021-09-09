#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    int numIslands(vector<vector<char>> &grid) {

        int ans = 0;
        int h = grid.size(), w = grid[0].size();
        for(int i = 0; i < h; i++) {
            for(int j = 0; j < w; j++) {
                if(grid[i][j] == '1') {
                    ans++;
                    remove_land(i, j, h, w, grid);
                }
            }
        }
		return ans;
    }
    void remove_land(int i, int j, int h, int w, vector<vector<char>> &grid) {
        if(i >= 0 && i < h && j >= 0 && j < w && grid[i][j] == '1') {
            grid[i][j] = '0';
            remove_land(i - 1, j, h, w, grid);
            remove_land(i, j + 1, h, w, grid);
            remove_land(i + 1, j, h, w, grid);
            remove_land(i, j - 1, h, w, grid);
        }
    }
};