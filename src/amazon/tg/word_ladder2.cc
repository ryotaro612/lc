#include <bits/stdc++.h>
using namespace std;
class Solution {
    /*
    "hit"
    "cog"
    ["hot","dot","dog","lot","log","cog"]
    
    "hit"
    "cog"
    ["hot","dot","dog","lot","log"]
    */
public:
    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> word_set;
        word_set.insert(beginWord);
        for(auto word: wordList)
            word_set.insert(word);
        if(word_set.find(endWord) == word_set.end())
            return {};
        vector<string> words(word_set.begin(), word_set.end());
        unordered_map<string, vector<string>> mp;
        for(int i =0;i<(int) words.size();i++) {
            for(int j = i + 1;j<(int) words.size(); j++) {
                if(is_neighbor(words[i], words[j])) {
                    mp[words[i]].push_back(words[j]);
                    mp[words[j]].push_back(words[i]);
                }
            }
        }
        const int inf = 1 << 29;
        unordered_map<string, int> d;
        for(auto word: words) {
            d[word] = inf;
        }
        queue<pair<string, int>> que;
        d[beginWord] = 0;
        que.push({beginWord, 0});
        
        while(!que.empty()) {
            string word = que.front().first;
            int dist = que.front().second;
            que.pop();
            if(d[word] < dist)
                continue;
            
            for(string &neigh: mp[word]) {
                if(dist + 1 < d[neigh]) {
                    d[neigh] = dist + 1;
                    que.push({neigh, d[neigh]});
                }
            }
        }
        /*
        for(auto a: d) {
            cout << a.first << " -> " << a.second << endl;
        }
        */
        
        if(d[endWord] == inf)
            return {};
        vector<vector<string>> res;
        find_paths(mp, d, {beginWord}, endWord, res);
        return res;
    }
    void find_paths(
        unordered_map<string, vector<string>> &mp, 
        unordered_map<string, int> &d, 
        vector<string> path,
        string &endWord,
        vector<vector<string>> &res) {
        if(path.back() == endWord) {
            res.push_back(path);
            return;
        }
        for(string &neigh: mp[path.back()]) {
            if(d[path.back()] + 1 == d[neigh]) {
                path.push_back(neigh);
                find_paths(mp, d, path, endWord, res);
                path.pop_back();
            }
        }
        
    }
    
    bool is_neighbor(string &a, string &b) {
        int n = a.size();
        int count = 0;
        for(int i = 0;i<n;i++) {
            if(a[i] != b[i])
                count++;
        }
        return count == 1;
    }
};
