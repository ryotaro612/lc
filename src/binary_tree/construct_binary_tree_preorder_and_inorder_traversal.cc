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
    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder) {
        unordered_map<int, int> mp;
        for(int i = 0; i < (int)inorder.size(); i++)
            mp[inorder[i]] = i;
        int index = 0;
        return rec(0, inorder.size(), index, mp, preorder, inorder);
    }

    TreeNode *rec(int left, int right, int &index, unordered_map<int, int> &mp,
                  vector<int> &preorder, vector<int> &inorder) {

        if(index == preorder.size())
            return nullptr;
        if(!(left <= mp[preorder[index]] && mp[preorder[index]] < right))
            return nullptr;
        TreeNode *res = new TreeNode(preorder[index]);
        int pivot = index;
        index++;
        res->left =
            rec(left, mp[preorder[pivot]], index, mp, preorder, inorder);
        res->right =
            rec(mp[preorder[pivot]] + 1, right, index, mp, preorder, inorder);
        return res;
    }
};