#include <bits/stdc++.h>
using namespace std;
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
class Solution {
  public:
    ListNode *reverseList(ListNode *head) {
        if(head == nullptr)
            return head;
        ListNode *tail = head, *res = nullptr;
        rec(head, res);
        head->next = nullptr;
        return res;
    }
    ListNode *rec(ListNode *node, ListNode *&res) {
        if(node->next == nullptr) {
            res = node;
            return node;
        }
        // cout << node->val << endl;
        ListNode *rev = rec(node->next, res);
        rev->next = node;
        return node;
    }
};