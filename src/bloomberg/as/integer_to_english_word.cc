#include <bits/stdc++.h>
using namespace std;
/*
123
12345
1234567
100
*/
class Solution {
  public:
    string numberToWords(int num) {
        if(num == 0)
            return "Zero";
        // 2147483647
        //        100
        string res;
        if(num >= 1000000000) {
            res = num3(num / 1000000000) + " Billion";
            num -= num / 1000000000 * 1000000000;
        }
        if(num >= 1000000) {
            string mi = num3(num / 1000000) + " Million";
            num -= num / 1000000 * 1000000;
            if((int)res.size() == 0)
                res = mi;
            else
                res += " " + mi;
        }

        if(num >= 1000) {
            string th = num3(num / 1000) + " Thousand";
            num -= num / 1000 * 1000;
            if((int)res.size() == 0)
                res = th;
            else
                res += " " + th;
        }
        if(num) {
            string uni = num3(num);
            if((int)res.size() == 0)
                res = uni;
            else
                res += " " + uni;
        }
        return res;
    }
    string num3(int num) {
        if(num < 100)
            return num2(num);
        string h = num09ToStr(num / 100) + " Hundred";
        num -= num / 100 * 100;
        if(num) {
            return h + " " + num2(num);
        }
        return h;
    }
    string num2(int num) {
        if(0 <= num && num <= 9)
            return num09ToStr(num);
        if(0 <= 10 && num <= 19)
            return num1019ToStr(num);
        string res = numDexToStr(num - num % 10);
        if(num % 10)
            res += " " + num09ToStr(num % 10);
        return res;
    }
    string num09ToStr(int num) {
        vector<string> res = {"Zero", "One", "Two",   "Three", "Four",
                              "Five", "Six", "Seven", "Eight", "Nine"};
        return res[num];
    }
    string num1019ToStr(int num) {
        vector<string> res = {"Ten",      "Eleven",  "Twelve",  "Thirteen",
                              "Fourteen", "Fifteen", "Sixteen", "Seventeen",
                              "Eighteen", "Nineteen"};
        return res[num - 10];
    }
    string numDexToStr(int num) {
        vector<string> res = {"Ten",   "Twenty",  "Thirty", "Forty", "Fifty",
                              "Sixty", "Seventy", "Eighty", "Ninety"};
        return res[num / 10 - 1];
    }
};