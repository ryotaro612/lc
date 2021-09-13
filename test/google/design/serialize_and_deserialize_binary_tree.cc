#include "google/design/serialize_and_deserialize_binary_tree.cc"
#include <gtest/gtest.h>

TEST(serialize_and_deserialize_binary_tree, 1) {
    Codec c;
    auto root = new TreeNode(1, new TreeNode(2),
                             new TreeNode(3, new TreeNode(4), new TreeNode(5)));
    string serial = c.serialize(root);
    auto decoded = c.deserialize(serial);

    EXPECT_EQ(1, decoded->val);
    EXPECT_EQ(2, decoded->left->val);
    EXPECT_EQ(nullptr, decoded->left->left);
    EXPECT_EQ(nullptr, decoded->left->right);
    EXPECT_EQ(3, decoded->right->val);
    EXPECT_EQ(4, decoded->right->left->val);
    EXPECT_EQ(nullptr, decoded->right->left->left);
    EXPECT_EQ(nullptr, decoded->right->left->right);
    EXPECT_EQ(5, decoded->right->right->val);
    EXPECT_EQ(nullptr, decoded->right->right->left);
    EXPECT_EQ(nullptr, decoded->right->right->right);
}

TEST(serialize_and_deserialize_binary_tree, 2) {
    Codec c;
    auto root = nullptr;
    string serial = c.serialize(root);
    auto decoded = c.deserialize(serial);
    EXPECT_EQ(nullptr, decoded);
}

TEST(serialize_and_deserialize_binary_tree, 3) {
    Codec c;
    auto root = new TreeNode(1);
    string serial = c.serialize(root);
    auto decoded = c.deserialize(serial);
    EXPECT_EQ(1, decoded->val);
    EXPECT_EQ(nullptr, decoded->left);
    EXPECT_EQ(nullptr, decoded->right);
}

TEST(serialize_and_deserialize_binary_tree, 4) {
    Codec c;
    auto root = new TreeNode(1, new TreeNode(2), nullptr);
    string serial = c.serialize(root);
    auto decoded = c.deserialize(serial);
    EXPECT_EQ(1, decoded->val);
    EXPECT_EQ(2, decoded->left->val);
    EXPECT_EQ(nullptr, decoded->left->left);
    EXPECT_EQ(nullptr, decoded->left->right);
    EXPECT_EQ(nullptr, decoded->right);
}

TEST(serialize_and_deserialize_binary_tree, 5) {
    Codec c;
    auto root =
        new TreeNode(1, 
		nullptr, new TreeNode(2, 
		nullptr, new TreeNode(3)));
    string serial = c.serialize(root);
    auto decoded = c.deserialize(serial);
    EXPECT_EQ(1, decoded->val);
    EXPECT_EQ(nullptr, decoded->left);
    EXPECT_EQ(2, decoded->right->val);
    EXPECT_EQ(nullptr, decoded->right->left);
    EXPECT_EQ(3, decoded->right->right->val);
    EXPECT_EQ(nullptr, decoded->right->right->left);
    EXPECT_EQ(nullptr, decoded->right->right->right);
}
