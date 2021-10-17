#include <bits/stdc++.h>
using namespace std;


class Solution {
public:
    bool backspaceCompare(string s, string t) {
        return normalize(s) == normalize(t);
    }

	string normalize(string s) {
		stack<char> stk;
        for(auto c: s) {
            if(c == '#') {
                if(!stk.empty())
                    stk.pop();
            } else {
                stk.push(c);
            }
        }
        string res;
        while(!stk.empty()) {
            res += stk.top();
            stk.pop();
        }
        reverse(res.begin(), res.end());
        return res;
	}
};