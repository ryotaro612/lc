#include <bits/stdc++.h>
using namespace std;
/*
"aa"
"a"

"aa"
"*"

"cb"
"?a"

"adceb"
"*a*b"

"acdcb"
"a*c?b"

"abcd"
"a**"

""
""

""
"*"
*/
class Solution {
  public:
    bool isMatch(string s, string p) {
        vector<vector<int>> cache(s.size(), vector<int>(p.size(), -1));
        return check(s, p, 0, 0, cache);
    }
    bool check(string &s, string &p, int index_s, int index_p,
               vector<vector<int>> &cache) {
        // cout << index_s << ", " << index_p << endl;
        if(index_s < s.size() && index_p < p.size()) {
            if(cache[index_s][index_p] >= 0)
                return cache[index_s][index_p];
        }
        if(s.size() == index_s) {
            if(p.size() == index_p) {
                return true;
            } else { // index_p < p.size()
                if(p[index_p] == '*')
                    return check(s, p, index_s, index_p + 1, cache);
                else
                    return false;
            }
        } else { // index_s < s.size()
            if(p.size() == index_p) {
                return false;
            } else {
                if(s[index_s] == p[index_p] || p[index_p] == '?') {
                    return cache[index_s][index_p] =
                               check(s, p, index_s + 1, index_p + 1, cache);
                } else if(p[index_p] == '*') {
                    return cache[index_s][index_p] =
                               check(s, p, index_s + 1, index_p, cache) ||
                               check(s, p, index_s, index_p + 1, cache) ||
                               check(s, p, index_s + 1, index_p + 1, cache);
                } else {
                    return cache[index_s][index_p] = false;
                }
            }
        }
    }
};