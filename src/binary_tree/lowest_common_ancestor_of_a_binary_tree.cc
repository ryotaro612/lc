#include <bits/stdc++.h>
using namespace std;
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
  public:
    TreeNode *lowestCommonAncestor(TreeNode *root, TreeNode *p, TreeNode *q) {
        vector<TreeNode *> p_lst, q_lst;
        rec(root, p_lst, p);
        rec(root, q_lst, q);
        unordered_set<TreeNode *> st(p_lst.begin(), p_lst.end());
        for(int i = q_lst.size() - 1; i >= 0; i--) {
            if(st.find(q_lst[i]) != st.end())
                return q_lst[i];
        }
        /*
        for(auto e: lst) {
            cout << e->val << endl;
        }
        */
        return nullptr;
    }
    void rec(TreeNode *node, vector<TreeNode *> &lst, TreeNode *q) {
        if(node == nullptr)
            return;
        if(node == q) {
            lst.push_back(q);
            return;
        }
        lst.push_back(node);
        rec(node->left, lst, q);
        if(lst.size() > 0) {
            if(lst.back() == q)
                return;
        }
        rec(node->right, lst, q);
        if(lst.size() > 0)
            if(lst.back() == q)
                return;
        lst.pop_back();
        return;
    }
};