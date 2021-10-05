#include <bits/stdc++.h>
using namespace std;

// Definition for a Node.
class Node {
  public:
    int val;
    Node *next;
    Node *random;

    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};

class Solution {
  public:
    Node *copyRandomList(Node *head) {
        if(head == nullptr)
            return nullptr;
        unordered_map<Node *, Node *> address_map;
        Node *res = new Node(head->val);
        address_map[head] = res;
        Node *cursor = res, *origin_cursor = head;
        while(origin_cursor->next != nullptr) {
            cursor->next = new Node(origin_cursor->next->val);
            address_map[origin_cursor->next] = cursor->next;
            cursor = cursor->next;
            origin_cursor = origin_cursor->next;
        }
        cursor = res;
        origin_cursor = head;
        if(origin_cursor->random != nullptr) {
            cursor->random = address_map[origin_cursor->random];
        }
        while(origin_cursor != nullptr) {
            if(origin_cursor->random != nullptr) {
                cursor->random = address_map[origin_cursor->random];
            }
            cursor = cursor->next;
            origin_cursor = origin_cursor->next;
        }

        return res;
    }
};