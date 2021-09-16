#include <bits/stdc++.h>
using namespace std;

class NumMatrix {

  public:
    int h, w;
    vector<vector<int>> bits;

    NumMatrix(vector<vector<int>> &matrix) {
        h = matrix.size();
        w = matrix[0].size();
        bits = vector<vector<int>>(h + 1, vector<int>(w + 1, 0));

        for(int i = 0; i < h; i++) {
            for(int j = 0; j < w; j++)
                add(i, j, matrix[i][j]);
        }
    }

    void update(int row, int col, int val) { 
        int current = sumRegion(row, col, row, col);
        add(row, col, val - current); 
    }

    int sumRegion(int row1, int col1, int row2, int col2) {
        int res = sum(row2, col2);
        if(col1 >= 1) {
            res -= sum(row2, col1 - 1);
        }
        if(row1 >= 1) {
            res -= sum(row1 - 1, col2);
        }
        if(col1 >= 1 && row1 >= 1) {
            res += sum(row1 - 1, col1 - 1);
        }
        return res;
    }

    int sum(int i, int j) {
        int res = 0;
        for(int bit_h = i + 1; bit_h > 0; bit_h -= bit_h & -bit_h) {
            for(int bit = j + 1; bit > 0; bit -= bit & -bit) {
                res += bits[bit_h][bit];
            }
        }
        return res;
    }
    void add(int i, int j, int v) {
        for(int bi = i + 1; bi <= h; bi += bi & -bi) {
            for(int b = j + 1; b <= w; b += b & -b) {
                bits[bi][b] += v;
            }
        }
    }
};