#include <bits/stdc++.h>
using namespace std;

class AutocompleteSystem {
  public:
    AutocompleteSystem(vector<string> &sentences, vector<int> &times)
        : sentences(sentences), times(times) {}

    vector<string> input(char c) {
        if(c == '#') {
            int n = times.size();
            bool done = false;
            for(int i = 0; i < n; i++) {
                if(sentences[i] == history) {
                    times[i]++;
                    done = true;
                    break;
                }
            }
            if(!done) {
                sentences.push_back(history);
                times.push_back(1);
            }
            history = "";
            return {};
        }
        history += c;
        vector<pair<int, string>> hits;
        for(int i = 0; i < (int)sentences.size(); i++) {
            if((int)history.size() > (int)sentences[i].size())
                continue;
            // history.size() <= sentence.size()
            int n = history.size();
            bool ok = true;
            for(int j = 0; j < n; j++) {
                if(history[j] != sentences[i][j])
                    ok = false;
            }
            if(ok) {
                hits.push_back({times[i], sentences[i]});
            }
        }
        sort(hits.begin(), hits.end(),
             [](const pair<int, string> &hitl, const pair<int, string> &hitr) {
                 if(hitl.first != hitr.first)
                     return hitl.first > hitr.first;
                 return hitl.second < hitr.second;
             });
        // cout << c << endl;
        // for(auto hit : hits) {
        //     cout << hit.second << endl;
        // }
        // cout << "==" << endl;
        vector<string> res;
        for(int i = 0; i < min((int)hits.size(), 3); i++)
            res.push_back(hits[i].second);
        return res;
    }

  private:
    vector<string> sentences;
    vector<int> times;
    string history;
};

/**
 * Your AutocompleteSystem object will be instantiated and called as such:
 * AutocompleteSystem* obj = new AutocompleteSystem(sentences, times);
 * vector<string> param_1 = obj->input(c);
 */

/*
input 
["AutocompleteSystem","input","input","input","input","input","input","input","input","input","input","input","input"]
[[["i love you","island","iroman","i love leetcode"],[5,3,2,2]],["i"],[" "],["a"],["#"],["i"],[" "],["a"],["#"],["i"],[" "],["a"],["#"]]

expected
[null,["i love you","island","i love leetcode"],["i love you","i love leetcode"],[],[],["i love you","island","i love leetcode"],["i love you","i love leetcode","i a"],["i a"],[],["i love you","island","i a"],["i love you","i a","i love leetcode"],["i a"],[]]
*/