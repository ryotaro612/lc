#include <bits/stdc++.h>
using namespace std;
/*
58 -> LVIII
1994 -> MCMXCIV
*/
class Solution {
  public:
    string intToRoman(int num) {
        string res = thousand(num / 1000);
        num -= num / 1000 * 1000;
        res += convert(num / 100, 'C', 'D', 'M');
        num -= num / 100 * 100;
        res += convert(num / 10, 'X', 'L', 'C');
        num -= num / 10 * 10;
        cout << num << endl;
        res += convert(num, 'I', 'V', 'X');
        return res;
    }
    string thousand(int value) { return string(value, 'M'); }
    string convert(int num, char one, char five, char ten) {
        if(num <= 3)
            return string(num, one);
        if(num == 4)
            return string(1, one) + string(1, five);
        if(num == 5)
            return string(1, five);
        if(num <= 8)
            return string(1, five) + string(num - 5, one);
        return string(1, one) + string(1, ten);
    }
};