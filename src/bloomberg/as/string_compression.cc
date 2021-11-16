#include <bits/stdc++.h>
using namespace std;
/*
["a","a","b","b","c","c","c"]
["a"]
["a","b","b","b","b","b","b","b","b","b","b","b","b"]
["a","a","a","b","b","a","a"]
*/
class Solution {
  public:
    int compress(vector<char> &chars) {
        int cursor = 0, count = 0;
        for(int i = 0; i < (int)chars.size(); i++) {
            /*
            cout << "i "<< i << " -> cursor" << cursor << " count" << count <<
            endl; for(auto c: chars) cout << c; cout << endl;
            */
            count++;
            if(i == (int)chars.size() - 1 || chars[i + 1] != chars[i]) {
                if(count == 1) {
                    chars[cursor++] = chars[i];
                } else if(1 < count) {
                    chars[cursor++] = chars[i];
                    string count_str = to_string(count);
                    for(auto digit : count_str) {
                        chars[cursor++] = digit;
                    }
                } else
                    assert(false);
                count = 0;
            }
        }
        while(cursor < chars.size()) {
            chars.pop_back();
        }
        return chars.size();
    }
};