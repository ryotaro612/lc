#include <bits/stdc++.h>
using namespace std;
class MedianFinder {
  public:
    multiset<int> ms;
    multiset<int>::iterator mid;
    /** initialize your data structure here. */
    MedianFinder() {}

    void addNum(int num) {
        ms.insert(num);
        int n = ms.size();
        if(n == 1) {
            mid = ms.begin();
            return;
        }
        if(n % 2 == 0) {
            if(*mid <= num) {
            } else { // *mid >= num
                mid--;
            }
        } else { // n % 2 == 1
            if(*mid <= num) {
                mid++;
            } else {
            }
        }
    }

    double findMedian() {
        int n = ms.size();
        if(n % 2 == 0) {
            return ((double)*mid + (double)*next(mid)) * 0.5;
        }
        return (double)*mid;
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */