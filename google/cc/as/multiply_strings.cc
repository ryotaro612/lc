#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

class Solution {
  public:
    string multiply(string num1, string num2) {
        string res = "0";
        int count = 0;
        for(int i = (int)num1.size() - 1; i >= 0; i--) {
            int c = num1[i] - '0';
            string temp = mul(num2, c);
            for(int j = 0; j < count; j++) {
                temp.push_back('0');
            }
            count++;
            res = add(res, temp);
        }
        return res;
    }

    string mul(string s, int d) {
        string res;
        int keta = 0;
        for(int i = s.size() - 1; i >= 0; i--) {
            int a = d * (s[i] - '0') + keta;
            res.push_back((a % 10) + '0');
            keta = a / 10;
        }
        if(keta > 0)
            res.push_back(keta + '0');
        reverse(res.begin(), res.end());
        return trim(res);
    }
    string add(string a, string b) {
        string aa = string(a), bb = string(b);
        reverse(aa.begin(), aa.end());
        reverse(bb.begin(), bb.end());
        if(bb.size() > aa.size())
            swap(aa, bb);

        while(aa.size() != bb.size()) {
            bb.push_back('0');
        }
        int keta = 0;
        string res;

        for(int i = 0; i < aa.size(); i++) {
            int c = aa[i] - '0', d = bb[i] - '0', e = (c + d) + keta;
            res.push_back((e % 10) + '0');
            keta = e / 10;
        }
        if(keta > 0)
            res.push_back(keta + '0');
        reverse(res.begin(), res.end());
        return trim(res);
    }

    string trim(string s) {
        for(int i = 0; i < s.size(); i++) {
            if(s[i] == '0')
                continue;

            return string(s.begin() + i, s.end());
        }
        return "0";
    }
};