#include <bits/stdc++.h>
using namespace std;
/*
["wrt","wrf","er","ett","rftt"] -> "wertf"
["z","x","z"] -> ""
["z","x"] -> "zx"
["aa"] -> "a"
["zy","zx"] -> "yxz"
["a","b","ca","cc"] -> "abc"
["abc","ab"] -> ""
https://kopricky.github.io/code/Graph/topological_sort.html
 */
class Solution {
  public:
    string alienOrder(vector<string> &words) {

        for(int i = 1; i < words.size(); i++) {
            for(int j = 0; j < i; j++) {
                if(words[i].size() < words[j].size()) {
                    int count = 0;
                    for(int k = 0; k < words[i].size(); k++) {
                        if(words[i][k] == words[j][k])
                            count++;
                    }
                    if((int)count == words[i].size())
                        return "";
                }
            }
        }

        unordered_map<char, unordered_set<char>> g = build_graph(words);
        // print_graph(g);
        return topological_sort(g);
    }
    unordered_map<char, unordered_set<char>>
    build_graph(vector<string> &words) {
        unordered_map<char, unordered_set<char>> g;
        set<char> alphabets;
        for(auto word : words)
            for(auto c : word)
                alphabets.insert(c);
        for(auto c : alphabets) {
            g[c] = unordered_set<char>();
        }
        for(int i = 1; i < (int)words.size(); i++) {
            int j = 0;
            while(words[i - 1][j] == words[i][j] && j < words[i - 1].size() &&
                  j < words[i].size()) {
                j++;
            }
            if(j < words[i - 1].size() && j < words[i].size() &&
               words[i - 1][j] != words[i][j]) {
                g[words[i - 1][j]].insert(words[i][j]);
            }
        }
        return g;
    }
    string topological_sort(unordered_map<char, unordered_set<char>> &g) {
        int count = 0;
        unordered_map<char, int> deg;
        for(auto from_tos : g) {
            deg[from_tos.first] = deg[from_tos.first];
            for(auto to : from_tos.second) {
                deg[to]++;
            }
        }
        queue<char> que;
        for(auto node_deg : deg) {
            if(node_deg.second == 0) {
                que.push(node_deg.first);
            }
        }
        string res;
        while(!que.empty()) {
            char node = que.front();
            que.pop();
            res.push_back(node);
            for(auto neighbor : g[node]) {
                if(--deg[neighbor] == 0) {
                    que.push(neighbor);
                }
            }
        }
        // cout << res << " | " << endl;
        for(auto node_deg : deg) {
            if(node_deg.second > 0)
                return "";
        }
        return res;
    }
    void print_graph(unordered_map<char, unordered_set<char>> &g) {
        for(auto e : g) {
            cout << e.first << " -> ";
            for(auto c : e.second)
                cout << c << " ";
            cout << endl;
        }
    }
};