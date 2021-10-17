#include "google/as/backspace_string_compare.cc"
#include <gtest/gtest.h>

TEST(backspace_string_compare, 1) {
    Solution s;
    EXPECT_TRUE(s.backspaceCompare("ab#c", "ad#c"));
}

