#include "google/ss/find_first_and_last_position_of_element_in_sorted_array.cc"
#include <gtest/gtest.h>

TEST(find_first_and_last_position_of_element_in_sorted_array, 1) {
    Solution s;
    vector<int> ans = {3, 4};
    vector<int> nums = {5, 7, 7, 8, 8, 10};
    EXPECT_EQ(ans, s.searchRange(nums, 8));
}

TEST(find_first_and_last_position_of_element_in_sorted_array, 2) {
    Solution s;
    vector<int> ans = {-1, -1};
    vector<int> nums = {2, 2};
    EXPECT_EQ(ans, s.searchRange(nums, 3));
}