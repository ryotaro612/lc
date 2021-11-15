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
    int kthSmallest(TreeNode *root, int k) {
        vector<int> order;
        rec(root, order);
        return order[k - 1];
    }
    void rec(TreeNode *node, vector<int> &order) {
        if(node == nullptr)
            return;
        rec(node->left, order);
        order.push_back(node->val);
        rec(node->right, order);
    }
};