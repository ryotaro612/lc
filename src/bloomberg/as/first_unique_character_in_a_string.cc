#include <bits/stdc++.h>
using namespace std;
class Solution {
  public:
    int firstUniqChar(string s) {
        unordered_map<char, int> freq;
        for(auto c : s)
            freq[c]++;
        //
        for(int i = 0; i < (int)s.size(); i++)
            if(freq[s[i]] == 1)
                return i;
        return -1;
    }
};