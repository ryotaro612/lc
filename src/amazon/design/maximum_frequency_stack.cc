#include <bits/stdc++.h>
using namespace std;

/**
["FreqStack","push","push","push","push","push","push","pop","push","pop","push","pop","push","pop","push","pop","pop","pop","pop","pop","pop"]
[[],[4],[0],[9],[3],[4],[2],[],[6],[],[1],[],[1],[],[4],[],[],[],[],[],[]]
*/
class FreqStack {
public:
  FreqStack() : max_freq(0) {}

  void push(int val) {
    int freq = ++val_freq[val];
    freq_vals[freq].push_back(val);
    if (max_freq < freq)
      max_freq = freq;
  }

  int pop() {
    // cout << "pop: ";
    int result = freq_vals[max_freq].back();
    // cout << result << endl;
    freq_vals[max_freq].pop_back();
    val_freq[result]--;
    if (freq_vals[max_freq].size() == 0) {
      freq_vals.erase(max_freq);
      max_freq--;
    }
    return result;
  }

private:
  int max_freq;
  unordered_map<int, int> val_freq;
  unordered_map<int, vector<int>> freq_vals;
};

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack* obj = new FreqStack();
 * obj->push(val);
 * int param_2 = obj->pop();
 */
