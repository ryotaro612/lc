#include "google/as/missing_ranges.cc"
#include <gtest/gtest.h>

TEST(missing_ranges, 1) {
    Solution s;
    vector<int> nums = {0, 1, 3, 50, 75};
    vector<string> ans = {"2", "4->49", "51->74", "76->99"};
    EXPECT_EQ(ans, s.findMissingRanges(nums, 0, 99));
}

TEST(missing_ranges, 2) {
    Solution s;
    vector<int> nums = {};
    vector<string> ans = {"1"};
    EXPECT_EQ(ans, s.findMissingRanges(nums, 1, 1));
}

TEST(missing_ranges, 3) {
    Solution s;
    vector<int> nums = {};
    vector<string> ans = {"-3->-1"};
    EXPECT_EQ(ans, s.findMissingRanges(nums, -3, -1));
}

TEST(missing_ranges, 4) {
    Solution s;
    vector<int> nums = {-1};
    vector<string> ans = {};
    EXPECT_EQ(ans, s.findMissingRanges(nums, -1, -1));
}

TEST(missing_ranges, 5) {
    Solution s;
    vector<int> nums = {-1};
    vector<string> ans = {"-2"};
    EXPECT_EQ(ans, s.findMissingRanges(nums, -2, -1));
}

TEST(missing_ranges, 6) {
    Solution s;
    vector<int> nums = {7};
    vector<string> ans = {"0->6", "8->9"};
    EXPECT_EQ(ans, s.findMissingRanges(nums, 0, 9));
}