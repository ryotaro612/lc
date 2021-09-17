#include "google/rec/android_unlock_patterns.cc"
#include <gtest/gtest.h>

TEST(android_unlock_patterns, 1) {
    Solution s;
    EXPECT_EQ(9, s.numberOfPatterns(1, 1));
}
TEST(android_unlock_patterns, 2) {
    Solution s;
    EXPECT_EQ(65, s.numberOfPatterns(1, 2));
}

TEST(android_unlock_patterns, 3) {
    Solution s;
    s.numberOfPatterns(3, 7);
}