#include<gtest/gtest.h>
#include "google/others/strobogrammatic_number.cc"


TEST(strobogrammatic_number, 1) {
	Solution s;
	EXPECT_EQ(true, s.isStrobogrammatic("69"));
}

TEST(strobogrammatic_number, 2) {
	Solution s;
	EXPECT_EQ(false, s.isStrobogrammatic("25"));
}

TEST(strobogrammatic_number, 3) {
	Solution s;
	EXPECT_EQ(true, s.isStrobogrammatic("69"));
}

TEST(strobogrammatic_number, 4) {
	Solution s;
	EXPECT_EQ(true, s.isStrobogrammatic("88"));
}

TEST(strobogrammatic_number, 5) {
	Solution s;
	EXPECT_EQ(false, s.isStrobogrammatic("962"));
}

TEST(strobogrammatic_number, 6) {
	Solution s;
	EXPECT_EQ(true, s.isStrobogrammatic("1"));
}