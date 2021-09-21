#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    vector<double> calcEquation(vector<vector<string>> &equations,
                                vector<double> &values,
                                vector<vector<string>> &queries) {
        unordered_map<string, int> indices;
        int num = 0;
        for(auto equation : equations) {
            if(indices.find(equation[0]) == indices.end())
                indices[equation[0]] = num++;
            if(indices.find(equation[1]) == indices.end())
                indices[equation[1]] = num++;
        }
        vector<int> par(num, -1);
        int eq_n = equations.size();
        for(int i = 0; i < eq_n; i++) {
            unite(indices[equations[i][0]], indices[equations[i][1]], par);
        }
        unordered_map<int, double> value_map;
        for(auto e : equations) {
            value_map[find_root(indices[e[0]], par)] = 1.0;
        }
        while(true) {
            bool update = false;
            for(int i = 0; i < eq_n; i++) {
                int numerator = indices[equations[i][0]],
                    denominator = indices[equations[i][1]];
                double value = values[i];
                if(value_map.find(numerator) == value_map.end()) {
                    if(value_map.find(denominator) != value_map.end()) {
                        value_map[numerator] = value_map[denominator] * value;
                        update = true;
                    }
                } else {
                    if(value_map.find(denominator) == value_map.end()) {
                        value_map[denominator] = value_map[numerator] / value;
                        update = true;
                    }
                }
            }
            if(!update)
                break;
        }
        int query_n = queries.size();
        vector<double> res(query_n, -1.0);
        for(int i = 0; i < query_n; i++) {
            string numerator = queries[i][0], denominator = queries[i][1];
            if(indices.find(numerator) != indices.end() &&
               indices.find(denominator) != indices.end() &&
               is_same(indices[numerator], indices[denominator], par)) {
                res[i] = value_map[indices[numerator]] /
                         value_map[indices[denominator]];
            }
        }
        return res;
    }

  private:
    int find_root(int index, vector<int> &par) {
        if(par[index] < 0)
            return index;
        return par[index] = find_root(par[index], par);
    }

    bool is_same(int a, int b, vector<int> &par) {
        return find_root(a, par) == find_root(b, par);
    }

    void unite(int a, int b, vector<int> &par) {
        int root_a = find_root(a, par), root_b = find_root(b, par);
        if(root_a == root_b)
            return;
        if(par[root_a] < par[root_b]) {
            par[root_a] += par[root_b];
            par[root_b] = root_a;
        } else {
            par[root_b] += par[root_a];
            par[root_a] = root_b;
        }
    }
};