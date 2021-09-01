#include "google/rec/word_squares.cc"
#include <gtest/gtest.h>

// Demonstrate some basic assertions.
TEST(word_squares, 1) {
    Solution s;
    vector<string> args = {"area", "lead", "wall", "lady", "ball"};
    vector<vector<string>> res = s.wordSquares(args);
    vector<vector<string>> ans = {{"ball", "area", "lead", "lady"},
                                  {"wall", "area", "lead", "lady"}};
    EXPECT_EQ(ans, res);
}