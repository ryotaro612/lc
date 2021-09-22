#include "google/others/my_calendar2.cc"
#include <gtest/gtest.h>

TEST(my_calendar2, 1) {
    auto s = MyCalendarTwo();

    vector<pair<int, int>> args = {{10, 20}, {50, 60}, {10, 40},
                                   {5, 15},  {5, 10},  {25, 55}};
    vector<bool> res;
    for(auto p : args) {
        res.push_back(s.book(p.first, p.second));
    }
    vector<bool> ans = {true, true, true, false, true, true};
    EXPECT_EQ(ans, res);
}

TEST(my_calendar2, 2) {
    auto s = MyCalendarTwo();
    vector<pair<int, int>> args = {{28, 46}, {9, 21},  {21, 39}, {37, 48},
                                   {38, 50}, {22, 39}, {45, 50}, {1, 12},
                                   {40, 50}, {31, 44}};
    vector<bool> res;
    for(auto p : args) {
        res.push_back(s.book(p.first, p.second));
    }
    vector<bool> ans = {true,  true, true, false, false,
                        false, true, true, false, false};
    EXPECT_EQ(ans, res);
}