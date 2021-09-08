#include "google/rec/strobogrammatic_number2.cc"
#include <gtest/gtest.h>

vector<string> normalize(vector<string> res) {
    set<string> s(res.begin(), res.end());
    return vector<string>(s.begin(), s.end());
}

TEST(strobogrammatic_number2, 1) {
    Solution s;

    vector<string> res = s.findStrobogrammatic(4);

    vector<string> ans = {"1001", "1111", "1691", "1881", "1961",
                          "6009", "6119", "6699", "6889", "6969",
                          "8008", "8118", "8698", "8888", "8968",
                          "9006", "9116", "9696", "9886", "9966"};
    EXPECT_EQ(normalize(ans), normalize(res));
}
