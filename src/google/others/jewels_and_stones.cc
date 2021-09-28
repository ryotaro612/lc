#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    int numJewelsInStones(string jewels, string stones) {
        unordered_set<char> jewels_set(jewels.begin(), jewels.end());

        int res = 0;
        for(auto stone : stones) {
            if(jewels_set.find(stone) != jewels_set.end())
                res++;
        }
        return res;
    }
};