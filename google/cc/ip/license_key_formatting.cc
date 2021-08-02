#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

class Solution {
  public:
    string licenseKeyFormatting(string s, int k) {
        string ss;
        for(int i = 0; i < s.size(); i++) {
            if(s[i] != '-')
                ss.push_back(toupper(s[i]));
        }
        if(ss.empty())
            return "";
        int offset = ss.size() % k == 0 ? k : ss.size() % k;
        string ans(ss.begin(), ss.begin() + offset);

        for(auto i = ss.begin() + offset;; i += k) {
            if(i == ss.end())
                break;
            ans += "-";
            ans += string(i, i + k);
        }
        return ans;
    }
};