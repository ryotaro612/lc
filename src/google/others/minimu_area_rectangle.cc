#include <bits/stdc++.h>
using namespace std;
class Solution {
  public:
    int minAreaRect(vector<vector<int>> &points) {
        unordered_map<int, set<int>> x_map;
        for(auto point : points) {
            x_map[point[0]].insert(point[1]);
        }
        const int inf = numeric_limits<int>::max();
        int res = inf;
        for(auto e1_iter = x_map.begin(); e1_iter != x_map.end(); e1_iter++) {
            for(auto e2_iter = next(e1_iter); e2_iter != x_map.end();
                e2_iter++) {
                pair<int, set<int>> e1 = *e1_iter;
                pair<int, set<int>> e2 = *e2_iter;
                vector<int> common_y;
                if(e1.second.size() < 2 || e2.second.size() < 2)
                    continue;
                set_intersection(e1.second.begin(), e1.second.end(),
                                 e2.second.begin(), e2.second.end(),
                                 back_inserter(common_y));
                sort(common_y.begin(), common_y.end());
                for(int k = 0; k < (int)common_y.size() - 1; k++) {
                    res = min(res, (common_y[k + 1] - common_y[k]) *
                                       abs(e2.first - e1.first));
                }
            }
        }
        return res == inf ? 0 : res;
    }
};