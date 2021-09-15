#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    string nextClosestTime(string time) {
        set<int> digits;
        digits.insert(time[0] - '0');
        digits.insert(time[1] - '0');
        digits.insert(time[3] - '0');
        digits.insert(time[4] - '0');

        vector<int> times;
        for(auto a : digits) {
            for(auto b : digits) {
                for(auto c : digits) {
                    for(auto d : digits) {
                        if(a == 2 && b <= 3 && c <= 5) {
                            times.push_back(a * 600 + b * 60 + c * 10 + d);
                        } else if(a <= 1 && c <= 5) {
                            times.push_back(a * 600 + b * 60 + c * 10 + d);
                        }
                    }
                }
            }
        }
        int bound = 600 * (time[0] - '0') + (time[1] - '0') * 60 +
                    (time[3] - '0') * 10 + (time[4] - '0');

        sort(times.begin(), times.end());
        auto found = upper_bound(times.begin(), times.end(), bound);
        int res;
        if(found == times.end()) {
            res = times[0];
        } else {
            res = *found;
        }
        return convert(res);
    }

  private:
    string convert(int v) {
        string res;
        int h = v / 60;
        if(h < 10)
            res.push_back('0');
        res += to_string(h);
        res.push_back(':');
        int m = v - (v / 60) * 60;
        if(m < 10)
            res.push_back('0');
        res += to_string(m);
        return res;
    }
};