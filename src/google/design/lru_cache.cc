#include <bits/stdc++.h>
using namespace std;

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 *
 */
class Node {
  public:
    Node *prev, *next;
    int key;
    int value;
    Node(int key, int value) : key(key), value(value) { prev = next = nullptr; }
};

class LRUCache {
  public:
    unordered_map<int, Node *> mp;
    int size, capacity;
    Node *head, *tail;

    LRUCache(int capacity) : capacity(capacity) {
        size = 0;
        head = tail = nullptr;
    }

    int get(int key) {
        Node *p = mp[key];
        if(p == nullptr)
            return -1;
        int found = p->value;
        // 先頭
        if(head == p)
            return found;
        // 要素が1個ではない
        if(p == tail)
            tail = p->prev;
        else
            p->next->prev = p->prev;
        p->prev->next = p->next;
        head->prev = p;
        p->next = head;
        p->prev = nullptr;
        head = p;
        return found;
    }

    void put(int key, int value) {
        if(size == 0) {
            head = new Node(key, value);
            mp[key] = head;
            tail = head;
            size++;
            return;
        }
        // TODO Nodeをmapにおく
        int found = get(key);
        if(found == -1) {
            if(size < capacity) {
                Node *node = new Node(key, value);
                head->prev = node;
                node->next = head;
                head = node;
                mp[key] = node;
                size++;
            } else { // 不要なやつをけす
                mp.erase(tail->key);
                mp[key] = tail;
                tail->value = value;
                tail->key = key;
                get(key);
            }
        } else { // 見つかった
            head->value = value;
        }
    }
    void debug() {
        if(head == nullptr)
            return;
        Node *p = head;
        while(p != nullptr) {
            cout << p << ", " << p->prev << " " << p->next << " " << p->key
                 << " " << p->value << endl;
            p = p->next;
        }
        cout << "----" << endl;
    }
};
