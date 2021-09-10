#include <bits/stdc++.h>
using namespace std;

/**
 * The read4 API is defined in the parent class Reader4.
 *
 */
int read4(char *buf4) { return -1; }

class Solution {

  public:
    Solution() {
        eof = false;
        que = queue<int>();

        buffer = (char *)malloc(sizeof(char) * 4);
    }
    int read(char *buf, int n) {
        char *p = buf;
        int read_num = 0;
        while(read_num < n) {
            if(!que.empty()) {
                *p = que.front();
                que.pop();
                p++;
                read_num++;
            } else {
				if(eof) {
					break;
				}
                int read4_num = read4(buffer);
                for(int i = 0; i < read4_num; i++) {
                    que.push(*(buffer + i));
                }
                if(read4_num < 4)
                    eof = true;
            }
        }
        return read_num;
    }
	~Solution() {
		free(buffer);
	}

  private:
    bool eof;
    queue<int> que;
	char *buffer;
};
