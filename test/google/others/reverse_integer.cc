#include "google/others/reverse_integer.cc"
#include <gtest/gtest.h>
TEST(reverse_integer, 1) {
    Solution s;
    EXPECT_EQ(321, s.reverse(123));
}

TEST(reverse_integer, 2) {
    Solution s;
    EXPECT_EQ(-321, s.reverse(-123));
}

TEST(reverse_integer, 3) {
    Solution s;
    EXPECT_EQ(21, s.reverse(120));
}

TEST(reverse_integer, 4) {
    Solution s;
    EXPECT_EQ(0, s.reverse(0));
}
TEST(reverse_integer, 5) {
    Solution s;
    EXPECT_EQ(0, s.reverse(1534236469));
}
TEST(reverse_integer, 6) {
    Solution s;
    EXPECT_EQ(-2143847412, s.reverse(-2147483412));
}