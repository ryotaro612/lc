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
    bool isValidBST(TreeNode *root) {
        if(root == nullptr)
            return true;
        return check(root, root->val);
    }
    bool check(TreeNode *root, int pivot) {
        if(root == nullptr)
            return true;
        if(root->left != nullptr) {
            if(pivot <= root->left->val)
                return false;
        }
        if(root->right != nullptr) {
            if(pivot >= root->right->val)
                return false;
        }
        return check(root->left, min(root->val, pivot)) &&
               check(root->right, max(root->val, pivot));
    }
};