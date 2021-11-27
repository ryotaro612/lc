#include <bits/stdc++.h>
using namespace std;
class Solution {
  public:
    string reverseWords(string s) {
        int n = s.size();
        vector<string> words;
        string word;
        for(int i = 0; i < n; i++) {
            if(s[i] == ' ')
                continue;
            word.push_back(s[i]);
            if(i == n - 1 || s[i + 1] == ' ') {
                words.push_back(word);
                word = "";
            }
        }
        reverse(words.begin(), words.end());
        string res;
        for(int i = 0; i < (int)words.size(); i++) {
            res.append(words[i]);
            if(i < (int)words.size() - 1)
                res.push_back(' ');
        }
        return res;
    }
};