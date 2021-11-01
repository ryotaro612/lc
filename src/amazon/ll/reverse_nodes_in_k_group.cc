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
    ListNode *reverseKGroup(ListNode *head, int k) {
        if(k == 1)
            return head;

        ListNode *res = head;
        for(int i = 0; i < k - 1; i++) {
            if(head->next == nullptr) {
                res = head;
                break;
            }
            res = res->next;
        }
        cout << res->val << endl;
        ListNode *left = head, *right = head, *prev_left = nullptr,
                 *prev_right = nullptr;
        int count = 0;
        for(;;) {
            if(right == nullptr) {
                if(count == k) {
                    rev(left, right);
                    if(prev_left != nullptr) {
                        prev_left->next = prev_right;
                    }
                }
                return res;
            } else {
                if(count < k) {
                    prev_right = right;
                    right = right->next;
                    count++;
                } else {
                    rev(left, right);
                    if(prev_left != nullptr) {
                        prev_left->next = prev_right;
                    }
                    prev_left = left;
                    left = right;
                    count = 0;
                }
            }
        }
        return res;
    }
    void rev(ListNode *left, ListNode *right) {
        if(left == right)
            return;
        ListNode *cur = left, *next_cur = left->next;
        while(true) {
            if(next_cur == right) {
                left->next = right;
                break;
            } else {
                ListNode *temp = next_cur->next;
                next_cur->next = cur;
                cur = next_cur;
                next_cur = temp;
            }
        }
    }
};