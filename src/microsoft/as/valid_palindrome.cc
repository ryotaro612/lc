#include <bits/stdc++.h>
using namespace std;
class Solution {
  public:
    bool isPalindrome(string s) {
        string a;
        for(auto c : s) {
            if('0' <= c && c <= '9' || 'a' <= c && c <= 'z' ||
               'A' <= c && c <= 'Z')
                a.push_back(tolower(c));
        }
        // cout << a << endl;
        for(int i = 0; i < (int)a.size() / 2; i++) {
            if(a[i] != a[(int)a.size() - 1 - i]) {
                // cout << i << " " << a[i] << " " << a[(int) a.size() - i];
                return false;
            }
        }
        return true;
    }
};