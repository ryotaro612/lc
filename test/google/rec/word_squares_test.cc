#include "google/rec/word_squares.cc"
#include <gtest/gtest.h>

TEST(word_squares, 1) {
    Solution s;
    vector<string> args = {"area", "lead", "wall", "lady", "ball"};
    vector<vector<string>> res = s.wordSquares(args);
    vector<vector<string>> ans = {{"ball", "area", "lead", "lady"},
                                  {"wall", "area", "lead", "lady"}};
    bool result = true;
    EXPECT_EQ(ans.size(), res.size());
    for(auto e : ans) {
        EXPECT_EQ(e, *find(res.begin(), res.end(), e));
    }
}

TEST(word_squares, 2) {
    Solution s;
    vector<string> args = {"abat", "baba", "atan", "atal"};
    vector<vector<string>> res = s.wordSquares(args);
    vector<vector<string>> ans = {{"baba", "abat", "baba", "atal"},
                                  {"baba", "abat", "baba", "atan"}};

    EXPECT_EQ(ans.size(), res.size());
    for(auto e : ans) {
        EXPECT_EQ(e, *find(res.begin(), res.end(), e));
    }
}
