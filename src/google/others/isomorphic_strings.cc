#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char> converter;
        int n = s.size();
        for(int i = 0; i < n; i++) {
            if(converter.find(s[i]) == converter.end()) {
                converter[s[i]] = t[i];
            } else {
                if(converter[s[i]] != t[i])
                    return false;
            }
        }
        set<char> count;
        for(auto e : converter) {
			count.insert(e.second);
        }
		if(count.size() != converter.size())
			return false;
        return true;
    }
};