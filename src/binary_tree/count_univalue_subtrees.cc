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
    int countUnivalSubtrees(TreeNode *root) {
        if(root == nullptr)
            return 0;
        int res = 0;
        unordered_set<int> st;
        rec(root, st, res);
        return res;
    }
    void rec(TreeNode *node, unordered_set<int> &st, int &res) {
        st.insert(node->val);
        if(node->left == nullptr) {
            if(node->right == nullptr) {
                res++;
                return;
            } else {
                unordered_set<int> right;
                rec(node->right, right, res);
                if(right.size() == 1 && right.find(node->val) != right.end())
                    res++;
                else {
                    for(auto e : right)
                        st.insert(e);
                }
                return;
            }
        } else {
            if(node->right == nullptr) {
                unordered_set<int> left;
                rec(node->left, left, res);
                if(left.size() == 1 && left.find(node->val) != left.end())
                    res++;
                else {
                    for(auto e : left)
                        st.insert(e);
                }
                return;
            } else {
                unordered_set<int> left, right;
                rec(node->left, left, res);
                rec(node->right, right, res);
                if(left.size() == 1 && right.size() == 1 &&
                   *left.begin() == *right.begin() &&
                   *left.begin() == node->val) {
                    res++;
                } else {
                    for(auto e : left)
                        st.insert(e);
                    for(auto e : right)
                        st.insert(e);
                }
                return;
            }
        }
    }
};