#include <bits/stdc++.h>
using namespace std;
// l* Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
  public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        string l1_str = to_str(l1), l2_str = to_str(l2);
        string zeros =
            string(abs((int)l1_str.size() - (int)l2_str.size()), '0');
        if(l1_str.size() < l2_str.size()) {
            l1_str = zeros + l1_str;
        } else if(l2_str.size() < l1_str.size()) {
            l2_str = zeros + l2_str;
        }
        int keta = 0;
        string sum;
        for(int i = l1_str.size() - 1; i >= 0; i--) {
            int v = l1_str[i] - '0' + l2_str[i] - '0' + keta;
            sum.push_back(v % 10 + '0');
            keta = v / 10;
        }
        if(keta)
            sum.push_back(1 + '0');
        reverse(sum.begin(), sum.end());
        // cout << sum << endl;
        ListNode *res = nullptr, *cursor;
        for(auto c : sum) {
            int digit = c - '0';
            if(res == nullptr) {
                res = new ListNode(digit);
                cursor = res;
            } else {
                cursor->next = new ListNode(digit);
                cursor = cursor->next;
            }
        }
        return res;
    }
    string to_str(ListNode *l) {
        ListNode *node = l;
        string res;
        while(node != nullptr) {
            res.push_back(node->val + '0');
            node = node->next;
        }
        return res;
    }
};