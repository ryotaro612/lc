#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    bool isValid(string s) {
        stack<char> stk;

        for(auto c : s) {
            if(stk.empty()) {
                stk.push(c);
            } else {
                char top = stk.top();
                if(top == '(' && c == ')' || top == '{' && c == '}' ||
                   top == '[' && c == ']')
                    stk.pop();
                else
                    stk.push(c);
            }
        }

        return stk.empty();
    }
};