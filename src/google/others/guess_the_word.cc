#include <bits/stdc++.h>
using namespace std;
// This is the Master's API interface.
// You should not implement it, or speculate about its implementation
class Master {
  public:
    Master(string expected, vector<string> wordlist)
        : expected(expected), time(0), ok(false) {
        words = unordered_set<string>(wordlist.begin(), wordlist.end());
    }
    int guess(string word) {
        time++;
        if(time <= 10 && word == expected)
            ok = true;
        if(words.find(word) == words.end())
            return -1;
        int count = 0;
        for(int i = 0; i < 6; i++)
            if(word[i] == expected[i])
                count++;
        return count;
    }

    bool is_ok() { return ok; }

  private:
    string expected;
    int time;
    bool ok;
    unordered_set<string> words;
};

class Solution {
  public:
    int match(string w1, string w2, int res = 0) {
        for(auto i = 0; i < w1.size(); ++i)
            if(w1[i] == w2[i])
                ++res;
        return res;
    }
    string bestCandidate(list<string> &words, vector<vector<int>> &probs,
                         int m_scr = 0, string best = "") {
        for(auto w : words) {
            int score = 1;
            for(auto i = 0; i < 6; ++i)
                score *= probs[i][w[i] - 'a'];
            if(score > m_scr)
                m_scr = score, best = w;
        }
        return best;
    }
    void findSecretWord(vector<string> &wordlist, Master &master, int res = 0) {
        vector<vector<int>> probs(6, vector<int>(26));
        list<string> remWords;
        for(auto w : wordlist) {
            remWords.push_back(w);
            for(auto i = 0; i < 6; ++i)
                probs[i][w[i] - 'a'] += 1;
        }
        while(res < 6) {
            auto candidate = bestCandidate(remWords, probs);
            res = master.guess(candidate);
            for(auto it = remWords.begin(); it != remWords.end();) {
                if(match(*it, candidate) != res) {
                    for(auto i = 0; i < 6; ++i)
                        probs[i][(*it)[i] - 'a'] -= 1;
                    it = remWords.erase(it);
                } else
                    ++it;
            }
        }
    }
};
/*
"ccoyyo"
["wichbx","oahwep","tpulot","eqznzs","vvmplb","eywinm","dqefpt","kmjmxr","ihkovg","trbzyb","xqulhc","bcsbfw","rwzslk","abpjhw","mpubps","viyzbc","kodlta","ckfzjh","phuepp","rokoro","nxcwmo","awvqlr","uooeon","hhfuzz","sajxgr","oxgaix","fnugyu","lkxwru","mhtrvb","xxonmg","tqxlbr","euxtzg","tjwvad","uslult","rtjosi","hsygda","vyuica","mbnagm","uinqur","pikenp","szgupv","qpxmsw","vunxdn","jahhfn","kmbeok","biywow","yvgwho","hwzodo","loffxk","xavzqd","vwzpfe","uairjw","itufkt","kaklud","jjinfa","kqbttl","zocgux","ucwjig","meesxb","uysfyc","kdfvtw","vizxrv","rpbdjh","wynohw","lhqxvx","kaadty","dxxwut","vjtskm","yrdswc","byzjxm","jeomdc","saevda","himevi","ydltnu","wrrpoc","khuopg","ooxarg","vcvfry","thaawc","bssybb","ccoyyo","ajcwbj","arwfnl","nafmtm","xoaumd","vbejda","kaefne","swcrkh","reeyhj","vmcwaf","chxitv","qkwjna","vklpkp","xfnayl","ktgmfn","xrmzzm","fgtuki","zcffuv","srxuus","pydgmq"]
10
*/