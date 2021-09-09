#include "google/ss/merge_intervals.cc"
#include <gtest/gtest.h>

TEST(merge_intervals, 1) {
    Solution s;
    vector<vector<int>> intervals = {{1, 4}, {5, 6}};
    vector<vector<int>> ans = {{1, 4}, {5, 6}};
    EXPECT_EQ(ans, s.merge(intervals));
}

TEST(merge_intervals, 2) {
    Solution s;
    vector<vector<int>> intervals = {{1, 3}, {2, 6}, {8, 10}, {15, 18}};
    vector<vector<int>> ans = {{1, 6}, {8, 10}, {15, 18}};
    EXPECT_EQ(ans, s.merge(intervals));
}

TEST(merge_intervals, 3) {
    Solution s;
    vector<vector<int>> intervals = {{1, 4}, {4, 5}};
    vector<vector<int>> ans = {{1, 5}};
    EXPECT_EQ(ans, s.merge(intervals));
}

TEST(merge_intervals, 4) {
    Solution s;
    vector<vector<int>> intervals = {{1, 4}, {0, 0}};
    vector<vector<int>> ans = {{0, 0}, {1, 4}};
    EXPECT_EQ(ans, s.merge(intervals));
}

TEST(merge_intervals, 5) {
    Solution s;
    vector<vector<int>> intervals = {{2, 3}, {5, 5}, {2, 2}, {3, 4}, {3, 4}};
    vector<vector<int>> ans = {{2, 4}, {5, 5}};
    EXPECT_EQ(ans, s.merge(intervals));
}
