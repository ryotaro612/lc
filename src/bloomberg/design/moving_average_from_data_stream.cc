#include <bits/stdc++.h>
using namespace std;
class MovingAverage {
  public:
    int size;
    int sum;
    queue<int> que;
    MovingAverage(int size) : size(size), sum(0) {}

    double next(int val) {
        que.push(val);
        sum += val;
        if(que.size() > size) {
            sum -= que.front();

            que.pop();
        }
        // cout << sum << endl;
        return (double)sum / (double)min(size, (int)que.size());
    }
};
