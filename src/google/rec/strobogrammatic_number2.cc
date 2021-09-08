#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

class Solution {
  public:
    vector<string> findStrobogrammatic(int n) {
        // 1, 6, 9, 8,
        // 0, 1 2 3 4 5 6 7, 8, 9
        /*
        候補になりそうなのは　0, 1, 6, 8, 9
        半分にする
        */
        if(n == 1) {
            return {"0", "1", "8"};
        }
        vector<string> half = {""};
        rec(n / 2, true, half);
        if(n % 2 == 1) {
            vector<string> mid;
            for(auto s : half) {
                mid.push_back(s + '0');
                mid.push_back(s + '1');
                mid.push_back(s + '8');
            }
            half = mid;
        }
        vector<string> ans;
        for(auto s : half) {
            string right;
            for(int i = 0; i < n / 2; i++) {
                if(s[i] == '6') {
                    right.push_back('9');
                } else if(s[i] == '9')
                    right.push_back('6');
                else
                    right.push_back(s[i]);
            }
            reverse(right.begin(), right.end());
            ans.push_back(s + right);
        }
        return ans;
    }

    void rec(int n, bool is_first, vector<string> &sv) {
        if(n == 0)
            return;
        vector<string> next_s;
        for(auto s : sv) {
            if(!is_first)
                next_s.push_back(s + '0');
            next_s.push_back(s + '1');
            next_s.push_back(s + '6');
            next_s.push_back(s + '8');
            next_s.push_back(s + '9');
        }
        sv = next_s;
        rec(n - 1, false, sv);
    }
};