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
    ~TreeNode() {
        if(left != nullptr)
            delete left;
        if(right != nullptr)
            delete right;
    }
};

class Solution {
  public:
    int countNodes(TreeNode *root) {
        if(root == nullptr)
            return 0;

        int lb = 0, ub = 50001;
        while(ub - lb > 1) {
            int mid = (ub + lb) / 2;
            vector<bool> paths = find_path(mid);
            if(exist(paths, root)) {
                lb = mid;
            } else
                ub = mid;
        }
        return lb;
    }

  private:
    vector<bool> find_path(int num) {
        vector<bool> left;

        while(num != 1) {
            left.push_back(num % 2 == 0);
            num /= 2;
        }
        reverse(left.begin(), left.end());
        return left;
    }
    bool exist(vector<bool> &path, TreeNode *node) {
        TreeNode *p = node;
        for(auto direction : path) {
            if(direction)
                p = p->left;
            else
                p = p->right;
            if(p == nullptr)
                return false;
        }
        return p != nullptr;
    }
};
