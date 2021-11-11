#include <bits/stdc++.h>
using namespace std;
class Node {
  public:
    int val;
    Node *left;
    Node *right;
    Node *next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node *_left, Node *_right, Node *_next)
        : val(_val), left(_left), right(_right), next(_next) {}
};

class Solution {
  public:
    Node *connect(Node *root) {
        queue<pair<Node *, int>> que;
        if(root == nullptr)
            return root;
        que.push({root, 0});
        while(!que.empty()) {
            Node *node = que.front().first;
            int depth = que.front().second;
            que.pop();
            if(node->left != nullptr)
                que.push({node->left, depth + 1});
            if(node->right != nullptr)
                que.push({node->right, depth + 1});
            if(!que.empty()) {
                if(depth == que.front().second) {
                    node->next = que.front().first;
                }
            }
        }
        return root;
    }
};