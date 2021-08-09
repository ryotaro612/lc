#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
class Solution {
  public:
    int maxArea(vector<int> &height) {
        int n = height.size();
        vector<int> stair = {height[0]};
        vector<int> index = {0};
        for(int i = 1; i < n; i++) {
            if(height[i] > stair[stair.size() - 1]) {
                stair.push_back(height[i]);
                index.push_back(i);
            }
        }
        vector<int> rev_index = {n - 1};
        vector<int> rev_stair = {height[n - 1]};
        for(int i = n - 2; i >= 0; i--) {
            if(height[i] > rev_stair[rev_stair.size() - 1]) {
                rev_stair.push_back(height[i]);
                rev_index.push_back(i);
            }
        }

        int ans = 0;
        for(int i = 0; i < rev_stair.size(); i++) {
            for(int j = 0; j < stair.size(); j++) {
                if(index[j] >= rev_index[i])
                    break;
                if(j > 0 && stair[j - 1] >= rev_stair[i])
                    break;

                int h = min(stair[j], rev_stair[i]);
                ans = max(ans, h * (rev_index[i] - index[j]));
            }
        }

        return ans;
    }
};
