#include <bits/stdc++.h>
using namespace std;
// Definition for a binary tree node.
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
    int maxPathSum(TreeNode *root) {
        int ans = -1001;
        rec(root, ans);
        return ans;
    }

    int rec(TreeNode *node, int &ans) {
        if(node == nullptr)
            return -1001;
        int l = -1001;
        if(node->left != nullptr) {
            l = rec(node->left, ans);
        }
        int r = -1001;
        if(node->right != nullptr) {
            r = rec(node->right, ans);
        }
        if(l <= 0) {
            if(r <= 0) {
                ans = max(node->val, ans);
                return node->val;
            } else { // r>0
                ans = max(node->val + r, ans);
                return node->val + r;
            }
        } else { // l > 0
            if(r <= 0) {
                ans = max(node->val + l, ans);
                return node->val + l;
            } else { // r > 0
                ans = max(node->val + r + l, ans);
                return node->val + max(r, l);
            }
        }
    }
};