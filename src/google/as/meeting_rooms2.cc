#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    int minMeetingRooms(vector<vector<int>> &intervals) {
        int mx = 1000002, n = intervals.size();
        vector<int> rooms(mx, 0);
        for(int i = 0; i < n; i++) {
            rooms[intervals[i][0]]++;
            rooms[intervals[i][1]]--;
        }
        for(int i = 1; i < mx; i++)
            rooms[i] += rooms[i - 1];

        int res = *max_element(rooms.begin(), rooms.end());
        return res;
    }
};