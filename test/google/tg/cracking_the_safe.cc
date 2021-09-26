#include "google/tg/cracking_the_safe.cc"
#include <gtest/gtest.h>

TEST(cracking_the_safe, 1) {

    Solution s;
    string res = s.crackSafe(1, 2);

    unordered_set<string> ans = {"01", "10"};
    EXPECT_TRUE(ans.find(res) != ans.end());
}

TEST(cracking_the_safe, 2) {

    Solution s;
    string res = s.crackSafe(2, 2);

    unordered_set<string> ans = {"01100", "00110"};
    EXPECT_TRUE(ans.find(res) != ans.end());
}

TEST(cracking_the_safe, 3) {

    Solution s;
    string res = s.crackSafe(3, 2);

    unordered_set<string> ans = {"0001011100"};
    EXPECT_TRUE(ans.find(res) != ans.end());
}