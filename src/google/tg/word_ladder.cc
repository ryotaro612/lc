#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    int ladderLength(string beginWord, string endWord,
                     vector<string> &wordList) {

        unordered_map<string, int> mp;
        int n = wordList.size() + 1;
        unordered_set<string> words;
        words.insert(beginWord);
        mp[beginWord] = 0;
        for(int i = 0; i < (int)wordList.size(); i++) {
            mp[wordList[i]] = i + 1;
            words.insert(wordList[i]);
        }

        vector<vector<int>> g(n);
        for(auto word : words) {
            for(int i = 0; i < (int)word.size(); i++) {
                for(int j = 0; j < 26; j++) {
                    string temp = word;
                    temp[i] = j + 'a';
                    if(temp == word)
                        continue;
                    auto found = words.find(temp);
                    if(found != words.end()) {
                        g[mp[word]].push_back(mp[temp]);
                        g[mp[temp]].push_back(mp[word]);
                    }
                }
            }
        }

        const int inf = 10000000;
        vector<int> d(n, inf);
        d[0] = 0;
        queue<pair<int, int>> que;
        que.push({0, 0});
        while(!que.empty()) {
            pair<int, int> p = que.front();
            que.pop();

            if(d[p.second] <= p.first)
                continue;
            for(int i = 0; i < g[p.second].size(); i++) {
                int node = g[p.second][i];
                d[node] = d[p.second] + 1;
                que.push({d[node], node});
            }
        }
        if(d[mp[endWord]] == inf) {
            return 0;
        } else
            return d[mp[endWord]];
    }
};