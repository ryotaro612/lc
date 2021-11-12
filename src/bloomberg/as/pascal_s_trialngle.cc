#include <bits/stdc++.h>
using namespace std;
class Solution {
  public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> pascal;
        pascal.push_back({1});
        for(int i = 1; i < numRows; i++) {
            // cout << i << endl;
            vector<int> row(i + 1);
            row[0] = row[i] = 1;
            // cout << i << "inner " << endl;
            for(int j = 1; j < i; j++) {
                // cout << j << " j" << endl;
                row[j] = pascal[i - 1][j - 1] + pascal[i - 1][j];
            }
            pascal.push_back(row);
        }
        return pascal;
    }
};