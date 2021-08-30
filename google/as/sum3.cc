#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

class Solution {
  public:
    vector<vector<int>> threeSum(vector<int> &nums) {
        int n = nums.size();
        if(n < 3)
            return {};
        vector<set<int>> mp(200001);
        vector<int> nm;
        for(int i = 0; i < n; i++) {
            set<int> *p = &mp[nums[i] + 100000];
            if((*p).size() < 3) {
                (*p).insert(nm.size());
                nm.push_back(nums[i]);
            }
        }
        set<vector<int>> ans;
        for(int i = 0; i < nm.size() - 1; i++) {
            for(int j = i + 1; j < nm.size(); j++) {
                int v = -nm[i] - nm[j];
                if(v + 100000 < 0 || v + 100000 > 200000)
                    continue;

                auto found = mp[100000 + v];
                if(found.upper_bound(j) != found.end()) {
                    vector<int> a = {nm[i], nm[j], -(nm[i] + nm[j])};
                    sort(a.begin(), a.end());
                    ans.insert(a);
                }
            }
        }
        vector<vector<int>> res(ans.begin(), ans.end());
        return res;
    }
};