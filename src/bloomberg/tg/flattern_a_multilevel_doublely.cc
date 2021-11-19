#include <bits/stdc++.h>
using namespace std;
class Node {
  public:
    int val;
    Node *prev;
    Node *next;
    Node *child;
};

class Solution {
  public:
    Node *flatten(Node *head) {
        vector<Node *> nodes;
        collect(head, nodes);
        int i = 1;
        Node *node = head;
        while(i < (int)nodes.size()) {
            node->child = nullptr;
            node->next = nodes[i];
            nodes[i]->prev = node;
            node = node->next;
            i++;
        }
        return head;
    }
    void collect(Node *node, vector<Node *> &nodes) {
        if(node == nullptr)
            return;
        nodes.push_back(node);
        collect(node->child, nodes);
        collect(node->next, nodes);
    }
};