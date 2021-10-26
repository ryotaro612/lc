#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right)
        : val(x), left(left), right(right) {}
};
class Solution {
  public:
    bool isSymmetric(TreeNode *root) {
        if(root == nullptr)
            return true;
        return isSame(root->left, root->right);
    }
    bool isSame(TreeNode *node1, TreeNode *node2) {
        if(node1 == nullptr)
            return node2 == nullptr;
        if(node2 == nullptr)
            return node1 == nullptr;
        if(node1->val != node2->val)
            return false;
        return isSame(node1->left, node2->right) &&
               isSame(node1->right, node2->left);
    }
};