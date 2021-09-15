#include <gtest/gtest.h>
#include "google/as/next_closest_time.cc"

TEST(next_closest_time, 1) {
	Solution s;
	EXPECT_EQ("19:39", s.nextClosestTime("19:34"));
}

TEST(next_closest_time, 2) {
	Solution s;
	EXPECT_EQ("22:22", s.nextClosestTime("23:59"));
}

TEST(next_closest_time, 3) {
	Solution s;
	EXPECT_EQ("01:33", s.nextClosestTime("01:32"));
}