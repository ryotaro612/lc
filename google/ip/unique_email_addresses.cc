#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

class Solution {
  public:
    int numUniqueEmails(vector<string> &emails) {
        set<string> normalized_mails;
        for(auto email : emails)
            normalized_mails.insert(normalize(email));

        return normalized_mails.size();
    }

    string normalize(string email) {
        string local = "";
        auto at = email.find('@');
        for(int i = 0; i < at; i++) {
            char c = email[i];
            if(c == '.')
                continue;
            if(c == '+')
                break;
            local.push_back(c);
        }
        auto domain = string(email.begin() + at, email.end());
        return local + domain;
    }
};