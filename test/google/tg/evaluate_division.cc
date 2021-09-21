#include "google/tg/evaluate_division.cc"
#include <gtest/gtest.h>

TEST(evaluate_division, 1) {
    Solution s;
    vector<vector<string>> equations = {{"a", "b"}, {"b", "c"}};
    vector<double> values = {2.0, 3.0};
    vector<vector<string>> queries = {
        {"a", "c"}, {"b", "a"}, {"a", "e"}, {"a", "a"}, {"x", "x"}};
    vector<double> res = s.calcEquation(equations, values, queries);
    vector<double> ans = {6.00000, 0.50000, -1.00000, 1.00000, -1.00000};
    EXPECT_EQ(ans, res);
}

TEST(evaluate_division, 2) {
    Solution s;
    vector<vector<string>> equations = {{"a", "b"}, {"b", "c"}, {"bc", "cd"}};
    vector<double> values = {1.5, 2.5, 5.0};
    vector<vector<string>> queries = {
        {"a", "c"}, {"c", "b"}, {"bc", "cd"}, {"cd", "bc"}};
    vector<double> res = s.calcEquation(equations, values, queries);
    vector<double> ans = {3.75000, 0.40000, 5.00000, 0.20000};
    EXPECT_EQ(ans, res);
}

TEST(evaluate_division, 3) {
    Solution s;
    vector<vector<string>> equations = {{"a", "b"}};
    vector<double> values = {0.5};
    vector<vector<string>> queries = {
        {"a", "b"}, {"b", "a"}, {"a", "c"}, {"x", "y"}};
    vector<double> res = s.calcEquation(equations, values, queries);
    vector<double> ans = {0.50000, 2.00000, -1.00000, -1.00000};
    EXPECT_EQ(ans, res);
}

TEST(evaluate_division, 4) {
    Solution s;
    vector<vector<string>> equations = {{"a", "b"}, {"e", "f"}, {"b", "e"}};
    vector<double> values = {3.4, 1.4, 2.3};
    vector<vector<string>> queries = {{"b", "a"}, {"a", "f"}, {"f", "f"},
                                      {"e", "e"}, {"c", "c"}, {"a", "c"},
                                      {"f", "e"}};
    vector<double> res = s.calcEquation(equations, values, queries);
    vector<double> ans = {0.29412,  10.94800, 1.00000, 1.00000,
                          -1.00000, -1.00000, 0.71429};
    EXPECT_EQ(ans.size(), res.size());
    for(int i = 0; i < (int)ans.size(); i++) {
        EXPECT_NEAR(ans[i], res[i], 0.0001);
    }
}
