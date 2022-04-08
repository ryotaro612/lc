#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  vector<int> prisonAfterNDays(vector<int> &cells, int n) {
    unordered_map<int, int> transitions;
    unordered_map<int, bool> visit;
    int current = encode(cells);
    while (true) {
      // cout << current << endl;;
      if (visit[current])
        break;
      visit[current] = true;
      int next_cells = next_step(current);
      transitions[current] = next_cells;
      current = next_cells;
    }
    int loop_size = 0;
    int loop_start = current;
    while (true) {
      loop_size++;
      current = transitions[current];
      if (current == loop_start)
        break;
    }
    current = encode(cells);
    for (int i = n - 1; 0 <= i; i--) {
      if (current == loop_start) {
        i %= loop_size;
      }
      current = transitions[current];
    }
    return decode(current);
  }
  int encode(vector<int> cells) {
    int result = 0;
    for (int i = 0; i < 8; i++)
      if (cells[i])
        result |= (1 << (7 - i));
    return result;
  }
  vector<int> decode(int cells) {
    vector<int> result(8, 0);
    for (int i = 0; i < 8; i++)
      if (cells & (1 << i))
        result[7 - i] = 1;
    return result;
  }

  int next_step(int cells) {
    int result = 0;
    for (int i = 1; i < 7; i++) {
      bool a = cells & (1 << (i - 1));
      bool b = cells & (1 << (i + 1));
      if (a == b)
        result |= 1 << i;
    }
    return result;
  }
};
