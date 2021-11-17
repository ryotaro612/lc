#include <bits/stdc++.h>
using namespace std;
/*
[1,1,1]
2
 [1,2,3]
3
 [1]
1
*/
class Solution {
  public:
    int subarraySum(vector<int> &nums, int k) {
        int n = nums.size(), sum = 0, res = 0;
        unordered_map<int, int> cache;
        cache[0] = 1;
        for(int i = 0; i < n; i++) {
            sum += nums[i];
            if(cache.find(sum - k) != cache.end())
                res += cache[sum - k];
            cache[sum]++;
        }
        return res;
    }
};