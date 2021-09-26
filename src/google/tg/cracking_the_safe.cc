#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    string crackSafe(int n, int k) {
        int length = calc_length(n, k);
        string password = calc_intial_password(n);
        unordered_set<string> pws;
		pws.insert(password);
        vector<string> pws_vec;
		pws_vec.push_back(password);
        rec(pws_vec, pws, k, length);

		string res = pws_vec[0];
		for(int i=1;i<length;i++) {
			res += pws_vec[i][n-1];
		}
		return res;
    }
    bool rec(vector<string> &pws_vec, unordered_set<string> &pws, int k, int length) {
        if(pws.size() != pws_vec.size())
			return false;
        if(pws_vec.size() == length)
			return true;
		
		vector<string> next_passwords = calc_next_passwords(pws_vec[pws_vec.size() - 1], k);
		for(auto pw: next_passwords) {
			if(pws.find(pw) !=pws.end())
				continue;
			pws_vec.push_back(pw);
			pws.insert(pw);
			if(rec(pws_vec, pws, k, length)) {
				return true;	
			} else {
				pws_vec.pop_back();
				pws.erase(pw);
			}
		}
		return false;
    }

    vector<string> calc_next_passwords(string s, int k) {
        string temp = string(s.begin() + 1, s.end());
        vector<string> res;
        for(int i = 0; i < k; i++) {
            res.push_back(temp + (char)(i + '0'));
        }
		return res;
    }

    int calc_length(int n, int k) {
        int res = 1;
        for(int i = 0; i < n; i++)
            res *= k;
        return res;
    }
    string calc_intial_password(int n) {
        string res;
        for(int i = 0; i < n; i++)
            res += '0';
        return res;
    }
};