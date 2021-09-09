#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    bool isStrobogrammatic(string num) {
        // 1, 8, 0, 6, 9
        // 0 -> 0,  1 -> 0, 2 -> 1,
        int n = num.size();
        for(int i = 0; i < n / 2; i++) {
            if(num[i] == num[n - 1 - i]) {
                if(num[i] != '0' && num[i] != '8' && num[i] != '1')
                    return false;
            } else if(num[i] == '6' && num[n - 1 - i] == '9') {
                continue;
            } else if(num[i] == '9' && num[n - 1 - i] == '6') {
                continue;
            } else
                return false;
        }
        if(n % 2 == 1) {
            switch(num[n / 2]) {
            case '1':
            case '8':
            case '0':
                return true;
            default:
                return false;
            }
        }
        return true;
    }
};