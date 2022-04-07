#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  vector<int> topKFrequent(vector<int> &nums, int k) {
    unordered_map<int, int> counter;
    for (int num : nums) {
      counter[num]++;
    }
    multiset<pair<int, int>> num_set;
    for (pair<int, int> num_count : counter) {
      int num = num_count.first;
      int count = num_count.second;
      if (static_cast<int>(num_set.size()) < k)
        num_set.insert({count, num});
      else {
        if ((*num_set.begin()).first < count) {
          num_set.erase(num_set.begin());
          num_set.insert({count, num});
        }
      }
    }
    vector<int> result;
    for (pair<int, int> count_num : num_set) {
      result.push_back(count_num.second);
    }
    return result;
  }
};
