//#define _GLIBCXX_DEBUG
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
        string ans = s_forward(s, n, tm), ans1 = s_backward(s, n, tm);
        cout << ans << endl;
        cout << ans1 << endl;
        if(ans.size() > ans1.size()) {
            return ans1;
        } else
            return ans;
    }

    string s_forward(string &s, int n, vector<int> &tm) {
        vector<int> count(52, 0);
        int s_end;
        for(int i = 0; i < n; i++) {
            count[enc(s[i])]++;
            bool ok = true;
            for(int j = 0; j < 52; j++) {
                if(count[j] < tm[j])
                    ok = false;
            }
            if(ok) {
                s_end = i;
                break;
            }
        }
        count = vector<int>(52, 0);
        for(int i = s_end; i >= 0; i--) {
            count[enc(s[i])]++;
            bool ok = true;
            for(int j = 0; j < 52; j++) {
                if(count[j] < tm[j])
                    ok = false;
            }
            if(ok) {
                return s.substr(i, s_end - i + 1);
            }
        }
        assert(false);
    }
    string s_backward(string &s, int n, vector<int> &tm) {
        vector<int> count(52, 0);
        int s_start;
        for(int i = n - 1; i >= 0; i--) {
            count[enc(s[i])]++;
            bool ok = true;
            for(int j = 0; j < 52; j++) {
                if(count[j] < tm[j])
                    ok = false;
            }
            if(ok) {
                s_start = i;
                break;
            }
        }
        count = vector<int>(52, 0);
        for(int i = s_start; i < n; i++) {
            count[enc(s[i])]++;
            bool ok = true;
            for(int j = 0; j < 52; j++) {
                if(count[j] < tm[j])
                    ok = false;
            }
            if(ok) {
                return s.substr(s_start, i - s_start + 1);
            }
        }
        assert(false);
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



//#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

class Solution {
  public:
    string minWindow(string s, string t) {
        vector<int> tm(52, 0);
        for(auto c : t) {
            tm[enc(c)]++;
        }
        int n = s.size();
        vector<vector<int>> sm(52, vector<int>(n + 1, 0));
        for(int i = 1; i < n + 1; i++) {
            sm[enc(s[i - 1])][i] = 1;
        }
        for(int i = 0; i < 52; i++) {
            for(int j = 1; j < n + 1; j++) {
                sm[i][j] += sm[i][j - 1];
            }
        }
        for(int i = 0; i < 52; i++) {
            if(sm[i][n] < tm[i]) {
                return "";
            }
        }
        int from = 0, to = n;
        for(int i = 0; i < n; i++) {
            bool ok = true;
            int tail = i;
            for(int j = 0; j < 52; j++) {
                auto found = lower_bound(sm[j].begin() + i, sm[j].end(),
                                         tm[j] + sm[j][i]);
                if(found == sm[j].end())
                    ok = false;
                else {
                    tail = max((int)distance(sm[j].begin(), found), tail);
                }
            }
            if(ok) {
                if(tail - i < to - from) {
                    from = i;
                    to = tail;
                }
            } else {
                break;
            }
        }
        return string(s.begin() + from, s.begin() + to);
    }

    int enc(char c) {
        if(isupper(c)) {
            return c - 'A' + 26;
        }
        return c - 'a';
    }
};
