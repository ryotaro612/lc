#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

class Solution {
  public:
    int lengthOfLongestSubstring(string s) {
        int ans = 0, n = s.size();
        if(n == 0)
            return 0;
        set<char> c;
        for(int i = 0, j = 0;;) {
            if(c.find(s[i]) == c.end()) {
                c.insert(s[i]);
                ans = max(ans, (int)c.size());
                if(i == n - 1)
                    break;
                else
                    i++;
            } else {
                c.erase(s[j]);
                j++;
            }
        }

        return ans;
    }
};