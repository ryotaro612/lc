#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
    TreeNode(int x, TreeNode *left, TreeNode *right)
        : val(x), left(left), right(right) {}
};

class Codec {
  public:
    // Encodes a tree to a single string.
    string serialize(TreeNode *root) {
        queue<TreeNode *> que;
        que.push(root);
        vector<string> nodes;
        while(!que.empty()) {
            TreeNode *node = que.front();
            que.pop();
            if(node == nullptr) {
                nodes.push_back("null");
                continue;
            }
            nodes.push_back(to_string(node->val));
            que.push(node->left);
            que.push(node->right);
        }

        return as_string(nodes);
    }

    // Decodes your encoded data to tree.
    TreeNode *deserialize(string data) {

        vector<int> nodes = parse(data);
        if(nodes.empty() || nodes[0] == -1001)
            return nullptr;
        queue<TreeNode *> que;
        TreeNode *root = new TreeNode(nodes[0]);
        int index = 1;
        que.push(root);
        while(index < nodes.size()) {
            TreeNode *node = que.front();
            que.pop();
            if(nodes[index] != -1001) {
                TreeNode *child = new TreeNode(nodes[index]);
                node->left = child;
                que.push(child);
            }
            index++;
            if(index < nodes.size() && nodes[index] != -1001) {
                TreeNode *child = new TreeNode(nodes[index]);
                node->right = child;
                que.push(child);
            }
            index++;
        }
        return root;
    }

  private:
    string as_string(vector<string> nodes) {
        int size = nodes.size();
        string res = "[";
        for(int i = 0; i < size; i++) {
            res += nodes[i];
            if(i != size - 1)
                res += ",";
        }
        return res + "]";
    }
    vector<int> parse(string &data) {
        int head = 1;
        vector<string> items;
        for(int i = 2; i < (int)data.size(); i++) {
            if(data[i] == ',' || data[i] == ']') {
                items.push_back(data.substr(head, i - head));
                head = i + 1;
            }
        }
        vector<int> res;
        for(auto item : items) {
            if(item == "null")
                res.push_back(-1001);
            else {
                res.push_back(stoi(item));
            }
        }
        return res;
    }
};
