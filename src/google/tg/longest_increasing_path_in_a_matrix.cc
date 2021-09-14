#include <bits/stdc++.h>
using namespace std;
class Solution {
  public:
    int longestIncreasingPath(vector<vector<int>> &matrix) {
        int h = matrix.size(), w = matrix[0].size();
        vector<pair<int, pair<int, int>>> cells(h * w);
        for(int i = 0; i < h; i++)
            for(int j = 0; j < w; j++)
                cells.push_back({matrix[i][j], {i, j}});

        sort(cells.begin(), cells.end(), greater<pair<int, pair<int, int>>>());
        vector<vector<int>> cache(h, vector<int>(w, 0));
        int ans = 0;
        for(auto cell : cells) {
            int i = cell.second.first, j = cell.second.second;
            int res = 1;
            if(i > 0) {
                if(matrix[i - 1][j] > matrix[i][j])
                    res = max(res, 1 + cache[i - 1][j]);
            }
            if(j < w - 1) {
                if(matrix[i][j + 1] > matrix[i][j])
                    res = max(res, 1 + cache[i][j + 1]);
            }
            if(i < h - 1) {
                if(matrix[i + 1][j] > matrix[i][j])
                    res = max(res, 1 + cache[i + 1][j]);
            }
            if(0 < j) {
                if(matrix[i][j - 1] > matrix[i][j])
                    res = max(res, 1 + cache[i][j - 1]);
            }
            cache[i][j] = res;

            ans = max(res, ans);
        }
        return ans;
    }
};
