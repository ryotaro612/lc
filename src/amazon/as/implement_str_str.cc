#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    int strStr(string haystack, string needle) {
        vector<int> dp(haystack.size(), -1);
        int h_n = haystack.size(), n_n = needle.size();
        if(n_n == 0)
            return 0;
        for(int i = 0; i < h_n; i++) {
            bool ok = true;
            if(h_n - i < n_n)
                break;
            for(int j = 0; j < n_n; j++) {
                if(haystack[i + j] != needle[j]) {
                    ok = false;
                    break;
                }
            }
            if(ok)
                return i;
        }
        return -1;
    }
};