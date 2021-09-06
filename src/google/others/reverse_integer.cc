#include <bits/stdc++.h>
using namespace std;

class Solution {
    // 2147483648
  public:
    int reverse(int x) {
        if(x == 0 || can_overflow(x))
            return 0;
        string s = to_string(x);
        if(s[0] == '-') {
            s = s.substr(1, s.size() - 1);
            std::reverse(s.begin(), s.end());
            int d = stoi(s);
            return -d;
        } else {
            std::reverse(s.begin(), s.end());
            int d = stoi(s);
            return d;
        }
    }
    bool can_overflow(int x) {
        string s = to_string(x);
        if(s[0] == '-')
            s = s.substr(1, s.size() - 1);

        std::reverse(s.begin(), s.end());
        if(s.size() < 10)
            return false;
        string boundary = "2147483649";
        for(int i = 0; i < (int)boundary.size(); i++) {
			if(s[i] - '0' == boundary[i] - '0')
				continue;
            if(s[i] - '0' < boundary[i] - '0')
                return false;
			else
				return true;
        }
        return true;
    }
};
