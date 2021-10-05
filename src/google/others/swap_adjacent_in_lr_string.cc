#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    bool canTransform(string start, string end) {
        int n = start.size();
        vector<pair<char, int>> lr_start, lr_end;
        for(int i = 0; i < n; i++) {
            if(start[i] == 'L' || start[i] == 'R')
                lr_start.push_back({start[i], i});
            if(end[i] == 'L' || end[i] == 'R')
                lr_end.push_back({end[i], i});
        }
        if(lr_start.size() != lr_end.size())
            return false;
        for(int i = 0; i < (int)lr_start.size(); i++) {
            if(lr_start[i].first != lr_end[i].first)
                return false;
			if(lr_start[i].first == 'L') {
				if(lr_start[i].second >= lr_end[i].second)
					continue;
				else
					return false;
			} else { // R
				if(lr_start[i].second <= lr_end[i].second)
					continue;
				else
					return false;
			}
        }

        return true;
    }
};