#include <bits/stdc++.h>
using namespace std;
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Codec {
  public:
    // Encodes a tree to a single string.
    string serialize(TreeNode *root) {
        unordered_map<unsigned long long, int> i_val;
        assign(root, 0, i_val);

        string serial;
        for(auto pair : i_val) {
            int indice = pair.first;
            int val = pair.second;
            if(serial.size() != 0)
                serial.push_back(',');
            serial.append(to_string(indice) + ">" + to_string(val));
        }
        // cout << serial << endl;
        return serial;
    }
    void assign(TreeNode *node, int indice,
                unordered_map<unsigned long long, int> &i_val) {
        if(node == nullptr)
            return;
        i_val[indice] = node->val;
        assign(node->left, indice * 2ll + 1ll, i_val);
        assign(node->right, indice * 2ll + 2ll, i_val);
    }

    // Decodes your encoded data to tree.
    TreeNode *deserialize(string data) {
        unordered_map<unsigned long long, int> i_val;
        string s;
        for(int i = 0; i < (int)data.size(); i++) {
            if(i == data.size() - 1 || data[i] == ',') {
                if(i == data.size() - 1)
                    s.push_back(data[i]);
                string indice, val;
                int j = 0;
                for(; s[j] != '>'; j++)
                    indice.push_back(s[j]);
                j++;
                for(; j < s.size(); j++)
                    val.push_back(s[j]);
                // cout << s << endl;
                // cout << indice << " -> " << val << endl;
                i_val[stoll(indice)] = stoi(val);
                s = "";
            } else {
                s.push_back(data[i]);
            }
        }
        TreeNode *root = rebuild(0, i_val);
        return root;
    }
    TreeNode *rebuild(int indice,
                      unordered_map<unsigned long long, int> &i_val) {
        if(i_val.find(indice) == i_val.end())
            return nullptr;
        TreeNode *node = new TreeNode(i_val[indice]);
        node->left = rebuild(indice * 2ll + 1ll, i_val);
        node->right = rebuild(indice * 2ll + 2ll, i_val);
        return node;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec* ser = new Codec();
// Codec* deser = new Codec();
// string tree = ser->serialize(root);
// TreeNode* ans = deser->deserialize(tree);
// return ans;