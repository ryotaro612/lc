#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    vector<int> spiralOrder(vector<vector<int>> &matrix) {
        vector<int> res;
        int m = matrix.size(), n = matrix[0].size();
        vector<vector<bool>> used(m, vector<bool>(n, false));
        pair<int, int> delta = {0, 1};
        for(int i = 0, x = 0, y = 0; i < n * m; i++) {
            res.push_back(matrix[y][x]);
            used[y][x] = true;
            int next_y = y + delta.first;
            int next_x = x + delta.second;
            if(0 <= next_y && next_y < m && 0 <= next_x && next_x < n &&
               !used[next_y][next_x]) {
                y = next_y;
                x = next_x;
            } else {
                delta = next_delta(delta);
                y += delta.first;
                x += delta.second;
            }
        }
        return res;
    }
    pair<int, int> next_delta(pair<int, int> delta) {
        if(delta.first == 0 && delta.second == 1)
            return {1, 0};
        if(delta.first == 1 && delta.second == 0)
            return {0, -1};
        if(delta.first == 0 && delta.second == -1)
            return {-1, 0};
        if(delta.first == -1 && delta.second == 0)
            return {0, 1};
        assert(false);
    }
};
