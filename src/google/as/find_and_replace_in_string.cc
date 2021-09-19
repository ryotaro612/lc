#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    string findReplaceString(string s, vector<int> &indices,
                             vector<string> &sources, vector<string> &targets) {
        int n = indices.size();
        if(n == 0)
            return s;
        vector<pair<int, pair<string, string>>> items(n);
        for(int i = 0; i < n; i++) {
            items[i] = {indices[i], {sources[i], targets[i]}};
        }
        sort(items.begin(), items.end());
        string res;
        int cursor = 0;
        for(int i = 0; i < n;) {
            int index = items[i].first;
            string source = items[i].second.first,
                   target = items[i].second.second;
            if(cursor < index) {
                res.push_back(s[cursor]);
                cursor++;
            } else if(cursor == index) {
                int len = s.size() - index;
                if(s.substr(index, min(len, (int)source.size())) == source) {
                    res += target;
                    cursor += source.size();
                }
                i++;
            } else { // cursor > index
                i++;
            }
        }
        while(cursor < (int)s.size()) {
            res.push_back(s[cursor++]);
        }
        return res;
    }
};