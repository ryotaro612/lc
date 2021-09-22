#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    bool isAnagram(string s, string t) {
        multiset<char> s_set, t_set;
        for(char c : s)
            s_set.insert(c);
        for(char c : t)
            t_set.insert(c);

        return s_set == t_set;
    }
};