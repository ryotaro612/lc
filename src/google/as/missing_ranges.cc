#include <bits/stdc++.h>
using namespace std;
class Solution {
  public:
    vector<string> findMissingRanges(vector<int> &nums, int lower, int upper) {
        queue<int> que;
        for(auto num : nums) {
            if(lower <= num && num <= upper)
                que.push(num);
        }
        vector<string> ans;
        int head = lower;
        while(!que.empty()) {
            int tail = que.front();
            que.pop();
            if(head < tail) {
                if(head == tail - 1) {
                    ans.push_back(to_string(head));
                } else {
                    ans.push_back(to_string(head) + "->" + to_string(tail - 1));
                }
                head = tail + 1;
            } else if(head == tail) {
                head++;
            } else { // head > tail
            }
        }
        if(head == upper) {
            ans.push_back(to_string(head));
        } else if(head < upper) {
            ans.push_back(to_string(head) + "->" + to_string(upper));
        }
        return ans;
    }
};
