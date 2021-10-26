#include <bits/stdc++.h>
using namespace std;

/*
 * 42
 *    -42
 * 4193 with words -> 4193
 * words and 987
 * -91283472332
 * "21474836460" -> 2147483647
 */
class Solution {
  public:
    int myAtoi(string s) {
        s = trim(s);
        if(s.size() == 0)
            return 0;

        int sign = 1;
        if(s[0] == '-' || s[0] == '+') {
            if(s[0] == '-')
                sign = -1;
            s = string(s.begin() + 1, s.end());
        }
        s = trim_zero(s);
        cout << s << endl;
        s = trim_tail(s);

        long long res = as_num(s);
        res *= sign;
        cout << "long " << res << endl;
        res = max(-2147483648ll, res);
        cout << res << endl;
        res = min(res, 2147483647ll);
        cout << res << endl;
        return (int)res;
    }
    string trim(string s) {
        int n = s.size();
        int i = 0;
        for(; i < n; i++) {
            if(s[i] != ' ')
                break;
        }
        return string(s.begin() + i, s.end());
    }
    string trim_zero(string s) {
        int i = 0;
        for(; i < (int)s.size(); i++) {
            if(s[i] != '0')
                break;
        }
        return string(s.begin() + i, s.end());
    }
    string trim_tail(string s) {
        string res;
        for(auto c : s) {
            if(c >= '0' && c <= '9') {
                res.push_back(c);
            } else
                break;
        }
        return res;
    }
    long long as_num(string s) {
        long long res = 0ll;
        for(auto c : s) {
            res *= 10ll;
            res += c - '0';
            if(res >= 2147483648ll)
                return 2147483648ll;
        }
        return res;
    }
};