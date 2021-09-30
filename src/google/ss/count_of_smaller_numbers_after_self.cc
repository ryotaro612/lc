#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    vector<int> countSmaller(vector<int> &nums) {
        int n = nums.size();
        vector<int> bit(32769, 0);
        for(int i = 0; i < n; i++) {
            nums[i] += 10002;
        }
        vector<int> res(n);
        for(int i = n - 1; i >= 0; i--) {
            res[i] = sum(nums[i] - 1, bit);
            add(nums[i], 1, bit);
        }
        return res;
    }

    int sum(int i, vector<int> &bit) {
        int res = 0;
        while(i > 0) {
            res += bit[i];
            i -= i & -i;
        }
        return res;
    }

    void add(int i, int x, vector<int> &bit) {
        while(i < bit.size()) {
            bit[i] += x;
            i += i & -i;
        }
    }
};