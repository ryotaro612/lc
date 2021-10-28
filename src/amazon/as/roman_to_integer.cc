#include <bits/stdc++.h>
using namespace std;
/*
"III" -> 3
 "IV" -> 4
  "IX" -> 9
  "LVIII" -> 58
  "MCMXCIV" -> 1994
*/
class Solution {
  public:
    int romanToInt(string s) {
        int res = pop(s, 'I', 'V', 'X');
        res += pop(s, 'X', 'L', 'C') * 10;
        res += pop(s, 'C', 'D', 'M') * 100;
        res += (int)s.size() * 1000;
        return res;
    }
    int pop(string &s, char one, char five, char ten) {
        if((int)s.size() == 0)
            return 0;
        int res = 0;
        while((int)s.size() > 0 && s.back() == one) {
            res++;
            s.pop_back();
        }
        if((int)s.size() == 0)
            return res;
        if(s.back() == five) {
            res += 5;
            s.pop_back();
        } else if(s.back() == ten) {
            res += 10;
            s.pop_back();
        }
        if((int)s.size() == 0 || s.back() != one)
            return res;
        s.pop_back();
        return --res;
    }
};