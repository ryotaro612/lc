#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

class Solution {
  public:
    int oddEvenJumps(vector<int> &arr) {
        int n = arr.size();
        vector<vector<bool>> dp(n, vector<bool>(2, false));
        dp[n - 1][0] = dp[n - 1][1] = true;
        vector<int> sorted;
        map<int, int> index;
        sorted.push_back(arr[n - 1]);
        index[arr[n - 1]] = n - 1;
        for(int i = n - 2; i >= 0; i--) {
            auto iter = lower_bound(sorted.begin(), sorted.end(), arr[i]);
            //cout << "->" << i << endl;

            if(iter != sorted.end()) {
                dp[i][0] = dp[index[*iter]][1];
                if(arr[i] == *iter) {
                    dp[i][1] = dp[index[*iter]][0];
                } else if(iter != sorted.begin()) {
                    dp[i][1] = dp[index[*(iter - 1)]][0];
                }
            } else {
                dp[i][1] = dp[index[*(iter - 1)]][0];
            }
            sorted.push_back(arr[i]);
            sort(sorted.begin(), sorted.end());
            index[arr[i]] = i;
        }
        /*
        for(int i = 0; i < n; i++) {
            cout << i << " (" << dp[i][0] << ", " << dp[i][1] << ")" << endl;
        }
        */

        int ans = 0;
        for(int i = 0; i < (int)arr.size(); i++)
            if(dp[i][0])
                ans++;
        return ans;
    }
};
/*
int main() {
    Solution s;
    vector<int> arr = {10, 13, 12, 14, 15};
    auto ans = s.oddEvenJumps(arr);
    cout << ans << endl;
    return 0;
}
*/