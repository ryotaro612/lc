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
    /*  [3,9,20,null,null,15,7] ->  [[3],[20,9],[15,7]]
     *  [1] -> [[1]]
     * [] -> []
     */
  public:
    vector<vector<int>> zigzagLevelOrder(TreeNode *root) {
        vector<vector<int>> depth_nodes;
        queue<pair<int, TreeNode *>> que;
        que.push({0, root});
        while(!que.empty()) {
            int depth = que.front().first;
            TreeNode *node = que.front().second;
            que.pop();
            if(node == nullptr)
                continue;
            if(depth_nodes.size() <= depth) {
                depth_nodes.push_back({});
            }
            depth_nodes[depth].push_back(node->val);
            que.push({depth + 1, node->left});
            que.push({depth + 1, node->right});
        }
        for(int i = 0; i < (int)depth_nodes.size(); i++) {
            if(i % 2 == 1) {
                reverse(depth_nodes[i].begin(), depth_nodes[i].end());
            }
        }
        return depth_nodes;
    }
};