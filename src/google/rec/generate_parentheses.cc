#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    vector<string> generateParenthesis(int n) {
        unordered_set<string> res;
        rec(n, n, "", res);
        return vector<string>(res.begin(), res.end());
    }

    void rec(int left, int right, string s, unordered_set<string> &res) {
        if(left == 0 && right == 0)
            res.insert(s);

        if(left == 0) {
            if(right == 0) {
                res.insert(s);
            } else {
                rec(left, right - 1, s + ")", res);
            }
        } else { // left > 0
            if(left == right) {
                rec(left - 1, right, s + "(", res);
            } else { // left < right
                rec(left - 1, right, s + "(", res);
                rec(left, right - 1, s + ")", res);
            }
        }
    }
};