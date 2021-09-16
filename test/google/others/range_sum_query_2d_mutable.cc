#include "google/others/range_sum_query_2d_mutable.cc"
#include <gtest/gtest.h>

TEST(range_sum_query_2d_mutable, 1) {

    vector<vector<int>> matrix = {{{3, 0, 1, 4, 2},
                                   {5, 6, 3, 2, 1},
                                   {1, 2, 0, 1, 5},
                                   {4, 1, 0, 1, 7},
                                   {1, 0, 3, 0, 5}}};
    NumMatrix s(matrix);
    EXPECT_EQ(4, s.sum(0, 2));
    EXPECT_EQ(24, s.sum(1, 3));
    EXPECT_EQ(38, s.sum(4, 3));
    EXPECT_EQ(8, s.sumRegion(2, 1, 4, 3));
    s.update(3, 2, 2);
    EXPECT_EQ(10, s.sumRegion(2, 1, 4, 3));
}

TEST(range_sum_query_2d_mutable, 2) {

    vector<vector<int>> matrix = {{1}};
    NumMatrix s(matrix);
    EXPECT_EQ(1, s.sumRegion(0, 0, 0, 0));
    s.update(0, 0, -1);
    EXPECT_EQ(-1, s.sumRegion(0, 0, 0, 0));
}