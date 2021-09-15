#include <bits/stdc++.h>
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
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {

        ListNode *l1_ptr = l1, *l2_ptr = l2, *ans = nullptr;
        vector<ListNode *> nodes;

        while(l1_ptr != nullptr || l2_ptr != nullptr) {
            if(l1_ptr == nullptr) {
                nodes.push_back(l2_ptr);
                l2_ptr = l2_ptr->next;
            } else if(l2_ptr == nullptr) {
                nodes.push_back(l1_ptr);
                l1_ptr = l1_ptr->next;
            } else {
                if(l1_ptr->val < l2_ptr->val) {
                    nodes.push_back(l1_ptr);
                    l1_ptr = l1_ptr->next;
                } else {
                    nodes.push_back(l2_ptr);
                    l2_ptr = l2_ptr->next;
                }
            }
        }
        int n = nodes.size();
		if(0 < n) {
			ans = nodes[0];
		}
        for(int i = 0; i < n; i++) {
			if(i == n-1) {
				nodes[i]->next = nullptr;
			} else
				nodes[i]->next = nodes[i+1];
        }
        return ans;
    }
};