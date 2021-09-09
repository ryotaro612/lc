#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    int candy(vector<int> &ratings) {

        priority_queue<pair<int, int>, vector<pair<int, int>>,
                       greater<pair<int, int>>>
            que;

        int n = ratings.size();
        for(int i = 0; i < n; i++) {
            que.push({ratings[i], i});
        }
        vector<int> candies(n, -1);
        while(!que.empty()) {
            pair<int, int> p = que.top();
            que.pop();
            int index = p.second;
            int num = 1;
            if(index > 0 && candies[index - 1] != -1 &&
               ratings[index - 1] < ratings[index]) {
                num = max(candies[index - 1] + 1, num);
            }
            if(index < n - 1 && candies[index + 1] != -1 &&
               ratings[index + 1] < ratings[index]) {
                num = max(candies[index + 1] + 1, num);
            }
            candies[index] = num;
        }
        int ans = 0;
        for(auto candy : candies)
            ans += candy;
		return ans;
    }
};