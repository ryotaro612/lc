#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    vector<int> findOrder(int numCourses, vector<vector<int>> &prerequisites) {

        vector<vector<int>> g(numCourses), rev_g(numCourses);
        for(auto pre : prerequisites) {
            g[pre[1]].push_back(pre[0]);
            rev_g[pre[0]].push_back(pre[1]);
        }
        vector<bool> taken(numCourses, false);
        queue<int> que;
        for(int i = 0; i < numCourses; i++) {
            if(rev_g[i].size() == 0)
                que.push(i);
        }
        vector<int> ans;
        while(!que.empty()) {
            int node = que.front();
            que.pop();
            bool ok = true;
            for(int i = 0; i < rev_g[node].size(); i++) {
                if(!taken[rev_g[node][i]])
                    ok = false;
            }
            if(ok) {
                if(!taken[node]) {
                    taken[node] = true;
                    ans.push_back(node);
                    for(int i = 0; i < g[node].size(); i++) {
                        que.push(g[node][i]);
                    }
                }
            }
        }
        for(int i = 0; i < numCourses; i++) {
            if(!taken[i])
                return {};
        }
        return ans;
    }
};