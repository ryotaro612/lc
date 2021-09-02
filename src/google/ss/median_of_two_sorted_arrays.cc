#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2) {
        int n = nums1.size() + nums2.size();
        // 奇数なら(n-1) / 2, 偶数なら(n-1) / 2 + (1+ (n-1) /2)の平均

        int index = (n - 1) / 2;

        int lb = -1000001, ub = 1000001;
        while(ub - lb > 1) {
            int mid = (ub + lb) / 2;

            auto iter1 = lower_bound(nums1.begin(), nums1.end(), mid);
            // num1にあるmidよりも小さい要素の数
            int small_1 = distance(nums1.begin(), iter1);
            // num2にあるmidよりも小さい要素の数
            auto iter2 = lower_bound(nums2.begin(), nums2.end(), mid);
            int small_2 = distance(nums2.begin(), iter2);
            // index + 1は中央値を含めた少ない側の数
            if(index + 1 <= small_1 + small_2)
                ub = mid;
            else
                lb = mid;
        }
        if(n % 2 == 1) {
            return lb;
        } else {
            auto iter1 = lower_bound(nums1.begin(), nums1.end(), ub);
            auto iter2 = lower_bound(nums2.begin(), nums2.end(), ub);
            // ubより小さい数
            int count =
                distance(nums1.begin(), iter1) + distance(nums2.begin(), iter2);
            if(index + 2 <= count) {
                return lb;
            }
            vector<int> cands;
            if(iter1 != nums1.end())
                cands.push_back(*iter1);
            if(iter2 != nums2.end())
                cands.push_back(*iter2);
            sort(cands.begin(), cands.end());
            return ((double)cands[0] + (double)lb) / 2.0;
        }
    }
};