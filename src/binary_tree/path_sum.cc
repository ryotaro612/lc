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
    bool hasPathSum(TreeNode *root, int targetSum) {
        if(root == nullptr)
            return false;
        return rec(root, 0, targetSum);
    }
    bool rec(TreeNode *node, int current, int targetSum) {
        if(node == nullptr)
            return current == targetSum;
        if(node->left == nullptr) {
            if(node->right == nullptr) {
                cout << 1 << endl;
                return current + node->val == targetSum;
            } else {
                cout << 2 << endl;
                return rec(node->right, current + node->val, targetSum);
            }
        } else {
            if(node->right == nullptr) {
                cout << 3 << endl;
                return rec(node->left, current + node->val, targetSum);
            } else {
                cout << 4 << endl;
                return rec(node->left, current + node->val, targetSum) ||
                       rec(node->right, current + node->val, targetSum);
            }
        }
    }
};