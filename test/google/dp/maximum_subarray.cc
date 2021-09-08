#include "google/dp/maximum_subarray.cc"
#include <gtest/gtest.h>

TEST(maximum_subarray, 1) {

    Solution s;
    vector<int> nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    EXPECT_EQ(6, s.maxSubArray(nums));
}

TEST(maximum_subarray, 2) {

    Solution s;
    vector<int> nums = {-1};
    EXPECT_EQ(-1, s.maxSubArray(nums));
}