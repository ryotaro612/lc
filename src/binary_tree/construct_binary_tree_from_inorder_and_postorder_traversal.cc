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
    TreeNode *buildTree(vector<int> &inorder, vector<int> &postorder) {
        TreeNode *res = new TreeNode(postorder[postorder.size() - 1]);
        unordered_map<int, int> mp;
        for(int i = 0; i < (int)inorder.size(); i++)
            mp[inorder[i]] = i;
        int post_index = postorder.size() - 1;
        return rec(0, inorder.size(), post_index, mp, inorder, postorder);
    }
    TreeNode *rec(int left, int right, int &post_index,
                  unordered_map<int, int> &mp, vector<int> &inorder,
                  vector<int> &postorder) {
        if(post_index < 0)
            return nullptr;
        int inorder_index = mp[postorder[post_index]];
        if(!(left <= inorder_index && inorder_index < right))
            return nullptr;
        TreeNode *res = new TreeNode(postorder[post_index]);
        post_index--;
        res->right =
            rec(inorder_index + 1, right, post_index, mp, inorder, postorder);
        res->left =
            rec(left, inorder_index, post_index, mp, inorder, postorder);
        return res;
    }
};
