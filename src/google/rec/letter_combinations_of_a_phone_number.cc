#include <bits/stdc++.h>
using namespace std;
class Solution {
  public:
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        vector<string> mapping = {"",    "",    "abc",  "def", "ghi",
                                  "jkl", "mno", "pqrs", "tuv", "wxyz"};
        rec("", 0, digits, mapping, res);
        return res;
    }

    void rec(string prefix, int index, string &digits, vector<string> &mapping,
             vector<string> &res) {
        int n = digits.size();
        if(index == n) {
            if(n == 0)
                return;
            res.push_back(prefix);
            return;
        }
        for(char letter : mapping[digits[index] - '0']) {
            prefix.push_back(letter);
            rec(prefix, index + 1, digits, mapping, res);
            prefix.pop_back();
        }
    }
};