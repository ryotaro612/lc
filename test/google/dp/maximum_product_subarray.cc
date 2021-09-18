#include "google/dp/maximum_product_subarray.cc"
#include <gtest/gtest.h>

TEST(maximum_product_subarray, 1) {
    Solution s;
    vector<int> nums = {2, 3, -2, 4};
    EXPECT_EQ(6, s.maxProduct(nums));
}

TEST(maximum_product_subarray, 2) {
    Solution s;
    vector<int> nums = {-2, 0, -1};
    EXPECT_EQ(0, s.maxProduct(nums));
}

TEST(maximum_product_subarray, 3) {
    Solution s;
    vector<int> nums = {-4, -3, -2};
    EXPECT_EQ(12, s.maxProduct(nums));
}