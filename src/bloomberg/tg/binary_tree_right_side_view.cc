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
    vector<int> rightSideView(TreeNode *root) {
        vector<int> res;
        if(root == nullptr)
            return {};
        queue<pair<TreeNode *, int>> que;
        que.push({root, 0});
        while(!que.empty()) {
            pair<TreeNode *, int> p = que.front();
            que.pop();
            if(p.second < res.size()) {
                res[p.second] = p.first->val;
            } else
                res.push_back(p.first->val);

            if(p.first->left != nullptr)
                que.push({p.first->left, p.second + 1});
            if(p.first->right != nullptr)
                que.push({p.first->right, p.second + 1});
        }
        return res;
    }
};