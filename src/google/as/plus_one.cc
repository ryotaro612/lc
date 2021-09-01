#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

class Solution {
  public:
    vector<int> plusOne(vector<int> &digits) {
        vector<int> ans;
        int keta = 1;
        for(int i = (int)digits.size() - 1; i >= 0; i--) {
            int res = digits[i] + keta;
            if(res > 9) {
                ans.push_back(res % 10);
                keta = 1;
            } else {
                ans.push_back(res);
                keta = 0;
            }
        }
		if(keta)
			ans.push_back(keta);
        reverse(ans.begin(), ans.end());
        return ans;
    }
};