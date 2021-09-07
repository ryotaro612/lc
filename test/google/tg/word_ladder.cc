#include "google/tg/word_ladder.cc"
#include <gtest/gtest.h>

TEST(word_ladder, 1) {
    Solution s;
    vector<string> wordList = {"hot", "dot", "dog", "lot", "log", "cog"};
    EXPECT_EQ(5, s.ladderLength("hit", "cog", wordList));
}

TEST(word_ladder, 2) {
    Solution s;
    vector<string> wordList = {"hot", "dot", "dog", "lot", "log"};
    EXPECT_EQ(0, s.ladderLength("hit", "cog", wordList));
}

TEST(word_ladder, 3) {
    Solution s;
    vector<string> wordList = {"a", "b", "c"};
    EXPECT_EQ(2, s.ladderLength("a", "c", wordList));
}

