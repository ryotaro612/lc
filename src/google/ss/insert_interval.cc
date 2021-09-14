#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    vector<vector<int>> insert(vector<vector<int>> &intervals,
                               vector<int> &newInterval) {

        int n = intervals.size();
        priority_queue<int, vector<int>, greater<int>> heads, tails;
        heads.push(newInterval[0]);
        tails.push(newInterval[1]);
        for(auto e : intervals) {
            heads.push(e[0]);
            tails.push(e[1]);
        }

        vector<vector<int>> ans;
        stack<int> stk;
        while(!tails.empty()) {
            if(stk.empty()) {
                stk.push(heads.top());
                heads.pop();
                continue;
            }
            if(heads.empty()) {
                int tail;
                while(!tails.empty()) {
                    tail = tails.top();
                    tails.pop();
                }
                int head;
                while(!stk.empty()) {
                    head = stk.top();
                    stk.pop();
                }
                ans.push_back({head, tail});
                return ans;
            }
            if(heads.top() < tails.top()) {
                stk.push(heads.top());
                heads.pop();
            } else if(heads.top() == tails.top()) {
                heads.pop();
                tails.pop();
            } else {
                int tail = tails.top();
                tails.pop();
                if(stk.size() == 1) {
                    ans.push_back({stk.top(), tail});
                }
                stk.pop();
            }
        }
        return ans;
    }
};