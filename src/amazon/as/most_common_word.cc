#include <bits/stdc++.h>
using namespace std;

/**
"Bob hit a ball, the hit BALL flew far after it was hit."
["hit"]

*/
class Solution {
public:
  string mostCommonWord(string paragraph, vector<string> &banned) {
    unordered_map<string, int> word_freq = computeFrequency(paragraph);

    for (string &word : banned) {
      if (word_freq.find(word) != word_freq.end()) {
        word_freq.erase(word);
      }
    }
    int max_freq = -1;
    string result;
    for (pair<string, int> item : word_freq) {
      if (max_freq < item.second) {
        result = item.first;
        max_freq = item.second;
      }
    }
    return result;
  }

  unordered_map<string, int> computeFrequency(string &paragraph) {
    string word;
    unordered_map<string, int> result;
    unordered_set<char> ignore = {' ', '"', '?', '!', '\'', ',', ';', '.'};
    for (char c : paragraph) {
      if (ignore.find(c) == ignore.end()) {
        word.push_back(tolower(c));
      } else {
        if (0 < word.size()) {
          result[word]++;
          word = "";
        }
      }
    }
    if (0 < word.size())
      result[word]++;
    return result;
  }
};
