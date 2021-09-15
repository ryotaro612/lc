#include "google/tg/decode_string.cc"
#include <gtest/gtest.h>

TEST(decode_string, 1) {
    Solution s;
    EXPECT_EQ("aaabcbc", s.decodeString("3[a]2[bc]"));
}

TEST(decode_string, 2) {
    Solution s;
    EXPECT_EQ("accaccacc", s.decodeString("3[a2[c]]"));
}

TEST(decode_string, 3) {
    Solution s;
    EXPECT_EQ("abcabccdcdcdef", s.decodeString("2[abc]3[cd]ef"));
}

TEST(decode_string, 4) {
    Solution s;
    EXPECT_EQ("abccdcdcdxyz", s.decodeString("abc3[cd]xyz"));
}