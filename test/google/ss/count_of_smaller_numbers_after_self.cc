#include "google/ss/count_of_smaller_numbers_after_self.cc"
#include <gtest/gtest.h>

TEST(count_of_smaller_numbers_after_self, 1) {
    Solution s;
    vector<int> nums = {5, 2, 6, 1}, ans = {2, 1, 1, 0};
    EXPECT_EQ(ans, s.countSmaller(nums));
}

TEST(count_of_smaller_numbers_after_self, 2) {
    Solution s;
    vector<int> nums = {-1}, ans = {0};
    EXPECT_EQ(ans, s.countSmaller(nums));
}

TEST(count_of_smaller_numbers_after_self, 3) {
    Solution s;
    vector<int> nums = {-1, -1}, ans = {0, 0};
    EXPECT_EQ(ans, s.countSmaller(nums));
}