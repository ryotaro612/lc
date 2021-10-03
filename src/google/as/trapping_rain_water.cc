#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    int trap(vector<int> &height) {
        int n = height.size();
        if(n <= 2)
            return 0;
        vector<int> left(n, 0), right(n, 0);

        for(int i = 0; i < n; i++) {
            if(i == 0)
                left[i] = height[i];
            else {
                if(left[i - 1] < height[i])
                    left[i] = height[i];
                else // left[i-1] >= height[i];
                    left[i] = left[i - 1];
            }
        }
        for(int i = n - 1; i >= 0; i--) {
            if(i == n - 1)
                right[i] = height[i];
            else {
                if(right[i + 1] < height[i])
                    right[i] = height[i];
                else
                    right[i] = right[i + 1];
            }
        }
        int res = 0;
        for(int i = 1; i < n - 1; i++) {
            if(left[i - 1] >= height[i] && right[i + 1] >= height[i]) {
				int temp = min(left[i - 1], right[i + 1]) - height[i];
                res += temp;
            }
        }
        return res;
    }
};