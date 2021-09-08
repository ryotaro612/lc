#include <bits/stdc++.h>
using namespace std;

class MinStack {
  public:
    stack<pair<int, int>> stack;
    /** initialize your data structure here. */
    MinStack() {}

    void push(int val) {
        if(stack.size() == 0) {
            stack.push({val, val});
			return;
		}
		
		stack.push({val, min(val, getMin())});
    }

    void pop() {
		stack.pop();
	}

    int top() {
		return stack.top().first;
	}

    int getMin() {
		return stack.top().second;
	}
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */