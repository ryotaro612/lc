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
    vector<vector<int>> levelOrder(TreeNode *root) {
        map<int, vector<int>> mp;
        rec(root, 0, mp);
        vector<vector<int>> res;
        for(auto e : mp) {
            res.push_back(e.second);
        }
        return res;
    }
    void rec(TreeNode *node, int depth, map<int, vector<int>> &mp) {
        if(node == nullptr)
            return;
        mp[depth].push_back(node->val);
        rec(node->left, depth + 1, mp);
        rec(node->right, depth + 1, mp);
    }
};