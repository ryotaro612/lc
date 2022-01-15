#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    /*
    "1.01" 
    "1.001"
    
    "0.1"
    "1.1"
    */
    int compareVersion(string version1, string version2) {
        vector<int> v1 = split(version1), v2 = split(version2);
        /*
        cout << "v1" << endl;
        for(auto v: v1)
                cout << v << endl;
        cout << "----" << endl;
        cout << "v2" << endl;
        for(auto v: v2)
                cout << v << endl;
        cout << "----" << endl;
        */
        int i = 0;
        for(;i<min(v1.size(), v2.size());i++) {
            if(v1[i] < v2[i]) {
                return -1;
            } else if(v2[i] < v1[i]) {
                return 1;
            }
        }
        if(v1.size() < v2.size()) {
            for(;i<(int) v2.size();i++) {
                if(0< v2[i]) {
                    return -1;
                }
            }
        }
        if(v2.size() < v1.size()) {
            for(;i<(int) v1.size();i++) {
                if(0< v1[i]) {
                    return 1;
                }
            }
        }
        return 0;
    }
    
    vector<int> split(string &version) {
        vector<int> res;
        string s;
        for(auto c: version) {
            if(c == '.') {
                res.push_back(stoi(s));
                s = "";
            } else {
                s.push_back(c);
            }
        }
        if((int) s.size() > 0)
            res.push_back(stoi(s));
        return res;
    }
};
