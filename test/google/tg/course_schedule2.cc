#include "google/tg/course_schedule2.cc"
#include <gtest/gtest.h>

// TEST(course_schedule2, 1) {

//     Solution s;
//     vector<vector<int>> prerequistes = {{1, 0}};
//     vector<int> res = s.findOrder(2, prerequistes);

//     vector<vector<int>> answers = {{0, 1}};
//     EXPECT_TRUE(find(answers.begin(), answers.end(), res) != answers.end());

// }

// TEST(course_schedule2, 2) {

//     Solution s;
//     vector<vector<int>> prerequistes = {{1, 0}, {2, 0}, {3, 1}, {3, 2}};
//     vector<int> res = s.findOrder(4, prerequistes);

//     vector<vector<int>> answers = {{0, 2, 1, 3}, {0, 1, 2, 3}};

//     EXPECT_TRUE(find(answers.begin(), answers.end(), res) != answers.end());
// }

TEST(course_schedule2, 3) {

    Solution s;
    vector<vector<int>> prerequistes = {};
    vector<int> res = s.findOrder(1, prerequistes);

    vector<vector<int>> answers = {{0}};

    EXPECT_TRUE(find(answers.begin(), answers.end(), res) != answers.end());
}