#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  vector<int> topKFrequent(vector<int> &nums, int k) {
    unordered_map<int, int> counter;
    for (int num : nums) {
      counter[num]++;
    }
    int n = counter.size();
    vector<pair<int, int>> num_count;
    for (pair<int, int> e : counter) {
      num_count.push_back(e);
    }
    /*
    for(auto e: num_count) {
        cout << "(" << e.first <<"," << e.second << ") ";
    }
    */
    // cout << endl;
    int left = 0, right = n - 1, pivot = num_count[0].second;
    while (true) {
      for (; left < right;) {
        if (num_count[left].second < pivot) {
          swap(num_count[left], num_count[right]);
          right--;
        } else if (pivot <= num_count[right].second) {
          swap(num_count[left], num_count[right]);
          left++;
        } else {
          left++;
          right--;
        }
      }
      /*
      cout << "pivot "<< pivot << ", left " << left << ", right " << right <<
      endl; for(auto e: num_count) { cout << "(" << e.first <<"," << e.second <<
      ") ";
      }
      cout << endl;
      */
      if (left + 1 < k) { // pivotが多きすぎる
        pivot = num_count[left].second;
        left = right;
        right = n - 1;
      } else if (left + 1 == k) { // k <= left
        break;
      } else { // k < left + 1 pivotが小さすぎる
        pivot = num_count[right].second;
        left = 0;
      }
    }
    vector<int> result(k);
    for (int i = 0; i < k; i++)
      result[i] = num_count[i].first;
    return result;
  }
};
