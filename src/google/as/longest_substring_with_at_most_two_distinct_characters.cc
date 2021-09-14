#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    int lengthOfLongestSubstringTwoDistinct(string s) {
        multiset<char> chars;
        int ans = 0, n = s.size(), head = 0, tail = 0;
        while(tail < n) {
            if(at_most1(chars) || chars.find(s[tail]) != chars.end()) {
                chars.insert(s[tail]);
                tail++;
                ans = max(tail - head, ans);
            } else { // だめ
                chars.erase(chars.find(s[head]));
                head++;
            }
        }
        return ans;
    }

  private:
    bool at_most1(multiset<char> chars) {
        if(chars.size() <= 1)
            return true;
        auto iter = chars.end();
        iter--;
        if(*chars.begin() == *(iter))
            return true;
        return false;
    };
};