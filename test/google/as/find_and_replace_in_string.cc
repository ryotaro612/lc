#include "google/as/find_and_replace_in_string.cc"
#include <gtest/gtest.h>

TEST(find_and_replace_in_string, 1) {

    Solution s;
    vector<int> indices = {0, 2};
    vector<string> sources = {"a", "cd"};
    vector<string> targets = {"eee", "ffff"};
    EXPECT_EQ("eeebffff",
              s.findReplaceString("abcd", indices, sources, targets));
}

TEST(find_and_replace_in_string, 2) {

    Solution s;
    vector<int> indices = {0, 2};
    vector<string> sources = {"ab", "ec"};
    vector<string> targets = {"eee", "ffff"};
    EXPECT_EQ("eeecd",
              s.findReplaceString("abcd", indices, sources, targets));
}