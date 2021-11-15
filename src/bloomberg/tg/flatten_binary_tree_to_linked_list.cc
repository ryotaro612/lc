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
    void flatten(TreeNode *root) {
        if(root == nullptr)
            return;
        TreeNode *tail = root;
        rec(root, tail);
    }
    void rec(TreeNode *node, TreeNode *&tail) {

        if(node->left == nullptr && node->right == nullptr) {
            tail = node;
            return;
        }
        if(node->left == nullptr) {
            tail = node;
        } else {
            rec(node->left, tail);
        }
        if(node->right == nullptr) {
            node->right = node->left;
            node->left = nullptr;
        } else { // node->right != nullptr;
            if(node->left == nullptr) {
                rec(node->right, tail);
            } else {
                tail->right = node->right;
                node->right = node->left;
                node->left = nullptr;
                tail = tail->right;
                rec(tail, tail);
            }
        }
    }
};
