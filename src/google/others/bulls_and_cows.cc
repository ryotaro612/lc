#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    string getHint(string secret, string guess) {
        unordered_map<char, int> secret_mp, guess_mp;
        int bulls = 0;
        int n = secret.size();
        for(int i = 0; i < n; i++) {
            if(secret[i] == guess[i]) {
                bulls++;
            } else {
                secret_mp[secret[i]]++;
                guess_mp[guess[i]]++;
            }
        }
        int cows = 0;
        for(auto e : secret_mp) {
            cows += min(secret_mp[e.first], guess_mp[e.first]);
        }
        return to_string(bulls) + "A" + to_string(cows) + "B";
    }
};