#include "google/others/swap_adjacent_in_lr_string.cc"
#include <gtest/gtest.h>

TEST(swap_adjacent_in_lr_string, 1) {
    Solution s;
    EXPECT_TRUE(s.canTransform("RXXLRXRXL", "XRLXXRRLX"));
}

TEST(swap_adjacent_in_lr_string, 2) {
    Solution s;
    EXPECT_FALSE(s.canTransform("X", "L"));
}

TEST(swap_adjacent_in_lr_string, 3) {
    Solution s;
    EXPECT_FALSE(s.canTransform("LLR", "RRL"));
}

TEST(swap_adjacent_in_lr_string, 4) {
    Solution s;
    EXPECT_TRUE(s.canTransform("XL", "LX"));
}

TEST(swap_adjacent_in_lr_string, 5) {
    Solution s;
    EXPECT_FALSE(s.canTransform("XLLR", "LXLX"));
}

TEST(swap_adjacent_in_lr_string, 6) {
    Solution s;
    EXPECT_FALSE(s.canTransform("XRRXRX", "RXLRRX"));
}

TEST(swap_adjacent_in_lr_string, 7) {
    Solution s;
    EXPECT_FALSE(s.canTransform("RXR", "XXR"));
}

TEST(swap_adjacent_in_lr_string, 8) {
    Solution s;
    EXPECT_TRUE(s.canTransform("XXXXXLXXXX", "LXXXXXXXXX"));
}
