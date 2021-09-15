#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    string decodeString(string s) {
        stack<char> stk;

        for(auto c : s) {
            if(c == ']') {
                decode(stk);
            } else {
                stk.push(c);
            }
        }
        string ans;
        while(!stk.empty()) {
            ans.push_back(stk.top());
            stk.pop();
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }

  private:
    void decode(stack<char> &stk) {
        string rep;
        while(stk.top() != '[') {
            rep.push_back(stk.top());
            stk.pop();
        }
        stk.pop();
        reverse(rep.begin(), rep.end());
        string num_str;
        while(!stk.empty() && '0' <= stk.top() && stk.top() <= '9') {
            num_str.push_back(stk.top());
            stk.pop();
        }
        reverse(num_str.begin(), num_str.end());
        int num = stoi(num_str);
        for(int i = 0; i < num; i++) {
            for(auto c : rep)
                stk.push(c);
        }
    }
};