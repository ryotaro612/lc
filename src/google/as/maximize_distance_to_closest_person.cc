#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    int maxDistToClosest(vector<int> &seats) {
        // 2つの配列を使う
        int n = seats.size();
        const int inf = 30000;
        vector<int> left(n, inf);
        for(int i = 0; i < n; i++) {
            if(seats[i]) {
                left[i] = 0;
            } else {
                if(i != 0) {
                    left[i] = left[i - 1] + 1;
                }
            }
        }
        vector<int> right(n, inf);
        for(int i = n - 1; i >= 0; i--) {
            if(seats[i]) {
                right[i] = 0;
            } else {
                if(i != n - 1) {
                    right[i] = right[i + 1] + 1;
                }
            }
        }
        int res = 0;
        for(int i = 0; i < n; i++) {
            res = max(res, min(left[i], right[i]));
        }
        return res;
    }
};