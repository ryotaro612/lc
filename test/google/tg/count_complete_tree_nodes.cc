#include "google/tg/count_complete_tree_nodes.cc"
#include <gtest/gtest.h>

TEST(count_complete_tree_nodes, 1) {
    Solution s;
    TreeNode *root =
        new TreeNode(1, new TreeNode(2, new TreeNode(4), new TreeNode(5)),
                     new TreeNode(3, new TreeNode(6), nullptr));
    EXPECT_EQ(6, s.countNodes(root));
	delete root;
}

TEST(count_complete_tree_nodes, 2) {
    Solution s;
    TreeNode *root = nullptr;
    EXPECT_EQ(0, s.countNodes(root));
}

TEST(count_complete_tree_nodes, 3) {
    Solution s;
    TreeNode *root = new TreeNode(1);
    EXPECT_EQ(1, s.countNodes(root));
	delete root;
}