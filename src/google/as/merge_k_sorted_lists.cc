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
    ListNode *mergeKLists(vector<ListNode *> &lists) {
        int n = lists.size();
        bool empty = true;
        vector<ListNode *> pointers(n, nullptr);
        const int inf = 100000;
        int min_value = inf, min_index;
        for(int i = 0; i < n; i++) {
            pointers[i] = lists[i];
            if(pointers[i] != nullptr) {
                if(pointers[i]->val < min_value) {
                    min_value = pointers[i]->val;
                    min_index = i;
                }
            }
        }
        if(min_value == inf)
            return nullptr;
        ListNode *res = new ListNode(min_value);
        ListNode *cursor = res;
        pointers[min_index] = lists[min_index]->next;

        while(true) {
            int min_value = inf, min_index;
            for(int i = 0; i < n; i++) {
                if(pointers[i] != nullptr) {
                    if(pointers[i]->val < min_value) {
                        min_value = pointers[i]->val;
                        min_index = i;
                    }
                }
            }
            if(min_value == inf)
                break;
            cursor->next = new ListNode(min_value);
            cursor = cursor->next;
            pointers[min_index] = pointers[min_index]->next;
        }

        return res;
    }
};