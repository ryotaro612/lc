#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

class Solution {
  public:
    void rotate(vector<vector<int>> &matrix) {
        int n = matrix.size();
        for(int i = 0; i < n / 2; i++) {
            for(int j = i; j < n - 1 - i; j++) {
                int a = matrix[i][j];
                int b = matrix[j][n - 1 - i];
                int c = matrix[n - 1 - i][n - 1 - j];
                int d = matrix[n - 1 - j][i];
                matrix[j][n - 1 - i] = a;
                matrix[n - 1 - i][n - 1 - j] = b;
                matrix[n - 1 - j][i] = c;
                matrix[i][j] = d;
            }
        }
    }
};
