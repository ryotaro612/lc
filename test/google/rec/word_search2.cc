#include "google/rec/word_search2.cc"
#include <gtest/gtest.h>

TEST(word_search2, 1) {

    Solution s;
    vector<vector<char>> grid = {{'o', 'a', 'b', 'n'},
                                 {'o', 't', 'a', 'e'},
                                 {'a', 'h', 'k', 'r'},
                                 {'a', 'f', 'l', 'v'}};
    vector<string> words = {"oa", "oaa"};
    vector<string> ans = {"oa", "oaa"};
    EXPECT_EQ(ans, s.findWords(grid, words));
}

TEST(word_search2, 2) {
    Solution s;
    vector<vector<char>> grid = {{'a', 'a'}};
    vector<string> words = {"aaa"};
    vector<string> ans = {};
    EXPECT_EQ(ans, s.findWords(grid, words));
}

TEST(word_search2, 3) {
    Solution s;
    vector<vector<char>> grid = {{'o', 'a', 'a', 'n'},
                                 {'e', 't', 'a', 'e'},
                                 {'i', 'h', 'k', 'r'},
                                 {'i', 'f', 'l', 'v'}};
    vector<string> words = {"oath", "pea", "eat", "rain"};
    vector<string> ans = {"eat", "oath"};
    EXPECT_EQ(ans, s.findWords(grid, words));
}

TEST(word_search2, 4) {
    Solution s;
    vector<vector<char>> grid = {{'a', 'b'}, {'c', 'd'}};
    vector<string> words = {"abcd"};
    vector<string> ans = {};
    EXPECT_EQ(ans, s.findWords(grid, words));
}