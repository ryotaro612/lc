#include <bits/stdc++.h>
using namespace std;
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
/*
[1,2,3,4,5]
2
4
[5]
1
1
[1,2,3]
1
3
*/
class Solution {
  public:
    ListNode *reverseBetween(ListNode *head, int left, int right) {
        if(left == right)
            return head;
        left--;
        right--;
        ListNode *node = head;
        ListNode *l_edge = nullptr;
        for(int i = 0; i < left; i++) {
            l_edge = node;
            node = node->next;
        }
        ListNode *left_origin = node;
        ListNode *next_node = node->next;
        for(int i = left; i < right; i++) {
            ListNode *next2 = next_node->next;
            next_node->next = node;
            node = next_node;
            next_node = next2;
        }
        if(l_edge != nullptr) {
            l_edge->next = node;
        }
        left_origin->next = next_node;
        if(left > 0)
            return head;
        return node;
    }
};