
class Solution {
public:
  int maxSumSubmatrix(vector<vector<int>> &matrix, int k) {
    int n_row = matrix.size();
    int n_col = matrix[0].size();
    vector<vector<int>> grid(n_row, vector<int>(n_col, 0));
    for (int i = 0; i < n_row; i++) {
      for (int j = 0; j < n_col; j++) {
        grid[i][j] = matrix[i][j];
        if (i == 0) {
          if (j > 0) {
            grid[i][j] += grid[i][j - 1];
          }
        } else { // i > 0
          if (j == 0) {
            grid[i][j] += grid[i - 1][j];
          } else {
            grid[i][j] += grid[i - 1][j] + grid[i][j - 1] - grid[i - 1][j - 1];
          }
        }
      }
    }
    /*
    for(int i = 0;i<n_row;i++) {
        for(int j = 0;j<n_col;j++)
            cout << grid[i][j] << " ";
        cout << endl;
    }
    cout << "=---" << endl;
    */
    int res = -1000000;
    for (int left = 0; left < n_col; left++) {
      for (int right = left; right < n_col; right++) {
        set<int> prefix = {0};
        for (int r = 0; r < n_row; r++) {
          int area = grid[r][right];
          if (left)
            area -= grid[r][left - 1];
          // cout << left << " " << right << " " << area << endl;
          auto found = prefix.lower_bound(area - k);
          if (found != prefix.end()) {
            res = max(res, area - *found);
          }
          prefix.insert(area);
        }
      }
    }
    return res;
  }
};
