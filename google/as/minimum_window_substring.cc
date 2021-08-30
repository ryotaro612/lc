#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

class Solution {
  public:
    string minWindow(string s, string t) {
        vector<int> tm(52, 0);
        for(auto a : t)
            tm[enc(a)]++;
        vector<int> sm(52, 0);
        int n = s.size();
        for(int i = 0; i < n; i++) {
            sm[enc(s[i])]++;
        }
        for(int i = 0; i < 52; i++) {
            if(tm[i] > sm[i])
                return "";
        }

        int head = 0, tail = 0;
        vector<int> count(52, 0);
        int a_head = 0, a_tail = n;
        while(head < n) {
            //cout << head << endl;
            bool ok = true;
            for(int i = 0; i < 52; i++) {
                if(count[i] < tm[i])
                    ok = false;
            }
            if(!ok) {
                //cout << "not ok " << head << " " << tail << endl;
                if(tail < n) {
                    count[enc(s[tail])]++;
                    tail++;
                } else { // tail >= n
                    break;
                }

            } else {
                //cout << "ok" << head << " " << tail << endl;
                if(tail - head < a_tail - a_head) {
                    a_head = head;
                    a_tail = tail;
                }
                count[enc(s[head])]--;
                head++;
            }
        }
        return s.substr(a_head, a_tail - a_head);
    }

    int enc(char c) {
        if(isupper(c)) {
            return c - 'A' + 26;
        }
        return c - 'a';
    }
};

int main() {
    Solution s;
    assert(s.minWindow("ADOBECODEBANC", "ABC") == "BANC");
    assert(s.minWindow("a", "a") == "a");
    assert(s.minWindow("a", "aa") == "");
    assert(s.minWindow("ab", "a") == "a");
    return 0;
}
