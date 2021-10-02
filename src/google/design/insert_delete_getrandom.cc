#include <bits/stdc++.h>
using namespace std;

class RandomizedSet {
  public:
    RandomizedSet() { s = unordered_set<int>(); }

    bool insert(int val) {
        if(s.find(val) == s.end()) {
            s.insert(val);
            return true;
        }
        return false;
    }

    bool remove(int val) {
        if(s.find(val) == s.end())
            return false;
        s.erase(val);
        return true;
    }

    int getRandom() {
        int rand_val = rand(), n = s.size();
        int cursor = rand_val % n;
		auto iter = s.begin();
		return *next(iter, cursor);
    }

  private:
    unordered_set<int> s;
};