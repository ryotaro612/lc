#include <bits/stdc++.h>
using namespace std;

int knows(int a, int b) { return -1; }
struct Cache {
    vector<vector<int>> cache;
    Cache(int n) { cache = vector<vector<int>>(n, vector<int>(n, -1)); }
    bool query(int a, int b) {
        if(cache[a][b] == -1)
            return cache[a][b] = knows(a, b);
        else
            return cache[a][b];
    }
};

class Solution {
  public:
    int findCelebrity(int n) {
        vector<bool> can_celebrity(n, true);
        Cache cache(n);
        for(int i = 0; i < n; i++) {
            if(!can_celebrity[i])
                continue;
            for(int j = n - 1; j >= 0; j--) {
                if(i == j)
                    continue;
                if(cache.query(i, j)) {
                    can_celebrity[i] = false;
                    break;
                } else
                    can_celebrity[j] = false;
            }
            if(can_celebrity[i]) {
                for(int j = n - 1; j >= 0; j--) {
                    if(i == j)
                        continue;
                    if(cache.query(j, i))
                        can_celebrity[j] = false;
                    else {
                        can_celebrity[i] = false;
                        break;
                    }
                }
                if(can_celebrity[i])
                    return i;
            }
        }
        return -1;
    }
};