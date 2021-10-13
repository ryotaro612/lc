#include "google/tg/most_stones_removed_with_same_row_or_column.cc"
#include <gtest/gtest.h>

TEST(most_stones_removed_with_same_row_or_column, 1) {
    Solution s;
    vector<vector<int>> stones = {{0, 0}, {0, 1}, {1, 0},
                                  {1, 2}, {2, 1}, {2, 2}};
    EXPECT_EQ(5, s.removeStones(stones));
}

TEST(most_stones_removed_with_same_row_or_column, 2) {
    Solution s;
    vector<vector<int>> stones = {{0, 0}, {0, 2}, {1, 1}, {2, 0}, {2, 2}};
    EXPECT_EQ(3, s.removeStones(stones));
}

TEST(most_stones_removed_with_same_row_or_column, 3) {
    Solution s;
    vector<vector<int>> stones = {{0, 0}};
    EXPECT_EQ(0, s.removeStones(stones));
}


