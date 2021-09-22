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
    int diameterOfBinaryTree(TreeNode *root) { int res = 0; 
	calc_depth(root, res);
	return res;	
	}

    int calc_depth(TreeNode *node, int &res) {
        if(node == nullptr)
            return 0;
        int left = calc_depth(node->left, res),
            right = calc_depth(node->right, res);
        res = max(res, left + right);

        return 1 + max(left, right);
    }
};