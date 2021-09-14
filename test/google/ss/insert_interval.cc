#include "google/ss/insert_interval.cc"
#include <gtest/gtest.h>

TEST(insert_interval, 1) {
    Solution s;
    vector<vector<int>> intervals = {{1, 3}, {6, 9}};
    vector<int> new_intervals = {10, 12};
    vector<vector<int>> res = s.insert(intervals, new_intervals);
    vector<vector<int>> ans = {{1, 3}, {6, 9}, {10, 12}};
    EXPECT_EQ(ans, res);
}

TEST(insert_interval, 2) {
    Solution s;
    vector<vector<int>> intervals = {{1, 3}, {6, 9}};
    vector<int> new_intervals = {2, 5};
    vector<vector<int>> res = s.insert(intervals, new_intervals);
    vector<vector<int>> ans = {{1, 5}, {6, 9}};
    EXPECT_EQ(ans, res);
}

TEST(insert_interval, 3) {
    Solution s;
    vector<vector<int>> intervals = {{1,2},{3,5},{6,7},{8,10},{12,16}};
    vector<int> new_intervals = {4, 8};
    vector<vector<int>> res = s.insert(intervals, new_intervals);
    vector<vector<int>> ans = {{1, 2}, {3, 10}, {12, 16}};
    EXPECT_EQ(ans, res);
}

TEST(insert_interval, 4) {
    Solution s;
    vector<vector<int>> intervals = {};
    vector<int> new_intervals = {5, 7};
    vector<vector<int>> res = s.insert(intervals, new_intervals);
    vector<vector<int>> ans = {{5, 7}};
    EXPECT_EQ(ans, res);
}

TEST(insert_interval, 5) {
    Solution s;
    vector<vector<int>> intervals = {{1, 5}};
    vector<int> new_intervals = {2, 3};
    vector<vector<int>> res = s.insert(intervals, new_intervals);
    vector<vector<int>> ans = {{1, 5}};
    EXPECT_EQ(ans, res);
}

TEST(insert_interval, 6) {
    Solution s;
    vector<vector<int>> intervals = {{1, 5}};
    vector<int> new_intervals = {2, 7};
    vector<vector<int>> res = s.insert(intervals, new_intervals);
    vector<vector<int>> ans = {{1, 7}};
    EXPECT_EQ(ans, res);
}