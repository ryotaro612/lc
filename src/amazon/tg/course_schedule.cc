#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> graph(numCourses, vector<int>());
        for(vector<int> prerequisite: prerequisites) {
            graph[prerequisite[1]].push_back(prerequisite[0]);
        }
        vector<bool> done(numCourses, false);
        for(int i = 0;i<numCourses;i++) {   
             unordered_set<int> visit;
             if(!isDag(i, visit, done, graph)) 
                 return false;
        }
        return true;
    }
    bool isDag(
        int node, unordered_set<int> &visit, vector<bool> &done, vector<vector<int>> &graph) {
        if(visit.find(node) != visit.end())
            return false;
        if(done[node])
            return true;
        int num_neighbors = static_cast<int>(graph[node].size());
        if(num_neighbors == 0) {
           return done[node] = true; 
        }
        visit.insert(node);
        for(int neighbor: graph[node]) {
            if(!isDag(neighbor, visit, done, graph)) {
                return false;
            }
        }
        visit.erase(node);
        return done[node] = true;
    }
    
};
