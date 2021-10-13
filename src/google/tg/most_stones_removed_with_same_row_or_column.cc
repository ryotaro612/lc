#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    int removeStones(vector<vector<int>> &stones) {
        int n = stones.size();
        queue<pair<int, int>> que;
        vector<bool> exist(n, true);
        int res = n;
        for(int i = 0; i < n; i++) {
            if(exist[i]) {
                res--;
                cout << i << endl;
                que.push({stones[i][0], stones[i][1]});
                exist[i] = false;
                while(!que.empty()) {
                    pair<int, int> stone = que.front();
                    que.pop();
                    for(int j = 0; j < n; j++) {
                        if(exist[j]) {
                            if(stones[j][0] == stone.first ||
                               stones[j][1] == stone.second) {
                                que.push({stones[j][0], stones[j][1]});
                                exist[j] = false;
                            }
                        }
                    }
                }
            }
        }
        return res;
    }
};