#include "google/ss/median_of_two_sorted_arrays.cc"
#include <gtest/gtest.h>

TEST(median_of_two_sorted_arrays, 1) {
    Solution s;
    vector<int> nums1 = {1, 3};
    vector<int> nums2 = {2};
    auto res = s.findMedianSortedArrays(nums1, nums2);

    EXPECT_NEAR(2.000, res, 0.00001);
}
TEST(median_of_two_sorted_arrays, 2) {
    Solution s;
    vector<int> nums1 = {1, 2};
    vector<int> nums2 = {3, 4};
    auto res = s.findMedianSortedArrays(nums1, nums2);

    EXPECT_NEAR(2.50000, res, 0.00001);
}

TEST(median_of_two_sorted_arrays, 3) {
    Solution s;
    vector<int> nums1 = {0, 0};
    vector<int> nums2 = {0, 0};
    auto res = s.findMedianSortedArrays(nums1, nums2);

    EXPECT_NEAR(0.00000, res, 0.00001);
}

TEST(median_of_two_sorted_arrays, 4) {
    Solution s;
    vector<int> nums1 = {};
    vector<int> nums2 = {1};
    auto res = s.findMedianSortedArrays(nums1, nums2);

    EXPECT_NEAR(1.00000, res, 0.00001);
}

TEST(median_of_two_sorted_arrays, 5) {
    Solution s;
    vector<int> nums1 = {2};
    vector<int> nums2 = {};
    auto res = s.findMedianSortedArrays(nums1, nums2);

    EXPECT_NEAR(2.00000, res, 0.00001);
}

TEST(median_of_two_sorted_arrays, 6) {
    Solution s;
    vector<int> nums1 = {2, 2, 4, 4};
    vector<int> nums2 = {2, 2, 4, 4};
    auto res = s.findMedianSortedArrays(nums1, nums2);

    EXPECT_NEAR(3.00000, res, 0.00001);
}

TEST(median_of_two_sorted_arrays, 7) {
    Solution s;
    vector<int> nums1 = {1};
    vector<int> nums2 = {1};
    auto res = s.findMedianSortedArrays(nums1, nums2);

    EXPECT_NEAR(1.00000, res, 0.00001);
}