#include "google/dp/longest_palindromic_substring.cc"
#include <gtest/gtest.h>
TEST(longest_palindromic_substring, 1) {

    Solution s;
    auto res = s.longestPalindrome("babad");
    EXPECT_EQ("bab", res);
}

TEST(longest_palindromic_substring, 2) {
    Solution s;
    auto res = s.longestPalindrome("cbbd");
    EXPECT_EQ("bb", res);
}
TEST(longest_palindromic_substring, 3) {
    Solution s;
    auto res = s.longestPalindrome("a");
    EXPECT_EQ("a", res);
}

TEST(longest_palindromic_substring, 4) {
    Solution s;
    auto res = s.longestPalindrome("ac");
    EXPECT_EQ("a", res);
}
TEST(longest_palindromic_substring, 5) {
    Solution s;
    auto res = s.longestPalindrome("bb");
    EXPECT_EQ("bb", res);
}