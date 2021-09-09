#include "google/tg/number_of_islands.cc"
#include <gtest/gtest.h>

TEST(number_of_islands, 1) {
    Solution s;
    vector<vector<char>> grid = {{'1', '1', '1', '1', '0'},
                                 {'1', '1', '0', '1', '0'},
                                 {'1', '1', '0', '0', '0'},
                                 {'0', '0', '0', '0', '0'}};
    EXPECT_EQ(1, s.numIslands(grid));
}
