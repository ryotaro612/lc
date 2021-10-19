#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    double mincostToHireWorkers(vector<int> &quality, vector<int> &wage,
                                int k) {
        int n = quality.size();
        vector<pair<int, int>> quality_wage(n);
        for(int i = 0; i < n; i++)
            quality_wage[i] = {quality[i], wage[i]};
        sort(quality_wage.begin(), quality_wage.end(),
             [](const pair<int, int> &qw1, const pair<int, int> &qw2) {
                 return qw1.second * qw2.first < qw2.second * qw1.first;
             });

        priority_queue<int> que;
        double res = 1 << 31 - 1;
        int sum = 0;
        for(int i = 0; i < n; i++) {
            // cout << quality_wage[i].first << " " << quality_wage[i].second <<
            // endl;
            que.push(quality_wage[i].first);
            sum += quality_wage[i].first;
            if(que.size() > k) {
                sum -= que.top();
                que.pop();
            }
            // cout << "sum: " << sum << endl;
            if(que.size() == k) {
                res = min(res, (double)sum * (double)quality_wage[i].second /
                                   (double)quality_wage[i].first);
            }
        }
        return res;
    }
};