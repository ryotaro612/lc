#include <bits/stdc++.h>
using namespace std;
class Solution {
  public:
    void merge(vector<int> &nums1, int m, vector<int> &nums2, int n) {
        int index_m = 0, index_n = 0;
        vector<int> nums;
        while(true) {
            if(index_m < m) {
                if(index_n < n) {
                    if(nums1[index_m] <= nums2[index_n]) {
                        nums.push_back(nums1[index_m++]);
                    } else {
                        nums.push_back(nums2[index_n++]);
                    }
                } else {
                    nums.push_back(nums1[index_m++]);
                }
            } else {
                if(index_n < n) {
                    nums.push_back(nums2[index_n++]);
                } else {
                    break;
                }
            }
        }
        for(int i = 0; i < n + m; i++)
            nums1[i] = nums[i];
    }
};