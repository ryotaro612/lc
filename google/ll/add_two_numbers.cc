#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

// Definition for singly-linked list.
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

        ListNode *a = l1, *b = l2;

        ListNode *ans = new ListNode();
        ListNode *peek = ans;
        int c = 0;
        while(true) {
            //cout << " doge " << endl;
            if(a != nullptr) {
                c += a->val;
                a = a->next;
            }
            if(b != nullptr) {
                c += b->val;
                b = b->next;
            }
            //cout << c  << " ";
            peek->val = (c % 10);
            c = c / 10;
           // cout << a->val << " " << b->val << endl;

            if(a == nullptr && b == nullptr)
                break;

            peek->next = new ListNode;
            peek = peek->next;
        }
        //cout << "end" << keta << endl;
        if(c > 0) {
			peek->next = new ListNode(c);
        }
		/*
        cout << (&ans)->val << (&ans)->next->val << (&ans)->next->next->val
             << endl;
        cout << ((&ans)->next->next->next == NULL ? "a" : "b") << endl;
		*/
        return ans;
    }
};