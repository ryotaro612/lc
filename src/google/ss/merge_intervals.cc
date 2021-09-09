#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    vector<vector<int>> merge(vector<vector<int>> &intervals) {

        vector<int> starts(10001, 0), ends(10001, 0);
        for(auto interval : intervals) {
            starts[interval[0]]++;
            ends[interval[1]]++;
        }
        stack<int> edge_stack;

        vector<vector<int>> ans;
        for(int i = 0; i < 10001; i++) {
            for(int j = 0; j < starts[i]; j++) {
                edge_stack.push(i);
            }
            for(int j = 0; j < ends[i]; j++) {
                if(edge_stack.size() == 1) {
                    ans.push_back({edge_stack.top(), i});
                }
                edge_stack.pop();
            }
        }
        return ans;
    }
};