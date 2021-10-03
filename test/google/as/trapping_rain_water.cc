#include "google/as/trapping_rain_water.cc"
#include <gtest/gtest.h>

TEST(trapping_rain_water, 1) {
    Solution s;
    vector<int> height = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
    EXPECT_EQ(6, s.trap(height));
}

TEST(trapping_rain_water, 2) {
    Solution s;
    vector<int> height = {4,2,0,3,2,5};
    EXPECT_EQ(9, s.trap(height));
}