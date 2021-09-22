#include <bits/stdc++.h>
using namespace std;

class MyCalendarTwo {
  public:
    MyCalendarTwo() {}

    bool book(int start, int end) {
        for(auto book : double_books) {
            int overlap_start = max(book.first, start),
                overlap_end = min(book.second, end);
            if(overlap_start < overlap_end) {
                return false;
            }
        }

        for(auto book : books) {
            int overlap_start = max(book.first, start),
                overlap_end = min(book.second, end);
            if(overlap_start < overlap_end) {
                double_books.push_back({overlap_start, overlap_end});
            }
        }
        books.push_back({start, end});
        return true;
    }

  private:
    vector<pair<int, int>> books, double_books;
};