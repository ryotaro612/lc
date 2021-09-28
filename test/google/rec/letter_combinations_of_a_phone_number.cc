#include <gtest/gtest.h>
#include "google/rec/letter_combinations_of_a_phone_number.cc"


TEST(letter_combinations_of_a_phone_number, 1) {

	Solution s;
	vector<string> res = s.letterCombinations("23");
	auto res_set = set<string>(res.begin(), res.end());
	set<string> ans = {"ad","ae","af","bd","be","bf","cd","ce","cf"};
	EXPECT_EQ(ans, res_set);
}

TEST(letter_combinations_of_a_phone_number, 2) {
	Solution s;
	vector<string> res = s.letterCombinations("");
	auto res_set = set<string>(res.begin(), res.end());
	set<string> ans = {};
	EXPECT_EQ(ans, res_set);
}

TEST(letter_combinations_of_a_phone_number, 3) {
	Solution s;
	vector<string> res = s.letterCombinations("2");
	auto res_set = set<string>(res.begin(), res.end());
	set<string> ans = {"a", "b", "c"};
	EXPECT_EQ(ans, res_set);
}