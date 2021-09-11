#include <gtest/gtest.h>
#include "google/others/bulls_and_cows.cc"

TEST(bulls_and_cows, 1) {
	Solution s;
	EXPECT_EQ("0A4B", s.getHint("1122", "2211"));
}

TEST(bulls_and_cows, 2) {
	Solution s;
	EXPECT_EQ("1A1B", s.getHint("1123", "0111"));
}

TEST(bulls_and_cows, 3) {
	Solution s;
	EXPECT_EQ("0A0B", s.getHint("1", "0"));
}

TEST(bulls_and_cows, 4) {
	Solution s;
	EXPECT_EQ("1A0B", s.getHint("1", "1"));
}