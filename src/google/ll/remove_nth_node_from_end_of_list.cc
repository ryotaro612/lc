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
    ListNode *removeNthFromEnd(ListNode *head, int n) {

        vector<ListNode *> nodes;

        ListNode *p = head;
        while(p != nullptr) {
            nodes.push_back(p);
            p = p->next;
        }
        int size = nodes.size();
        // nodes[size-n]を削除する
        if(size - n - 1 >= 0) {
            if(size - n + 1 <= size - 1)
                nodes[size - n - 1]->next = nodes[size - n + 1];
            else
                nodes[size - n - 1]->next = nullptr;
        } else {
            head = head->next;
        }

        return head;
    }
};