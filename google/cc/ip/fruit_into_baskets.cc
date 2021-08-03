#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
class Solution {
  public:
    int totalFruit(vector<int> &fruits) {
        int type = -1, type2 = -1;
        int count = 0, count2 = 0;
        int ans = 0;
        for(int i = 0; i < (int)fruits.size();) {
            if(type == -1) {
                type = fruits[i];
                count++;
                ans = max(ans, count + count2);
                i++;
            } else if(fruits[i] == type) {
                count++;
                ans = max(ans, count + count2);
                i++;
            } else if(type2 == -1) {
                type2 = fruits[i];
                count2++;
                ans = max(ans, count + count2);
                i++;
            } else if(fruits[i] == type2) {
                count2++;
                ans = max(ans, count + count2);
                i++;
            } else { // 種類があふれた。
                int drop = i - count - count2;
                if(fruits[drop] == type) {
                    count--;
                    if(count == 0)
                        type = -1;
                } else {
                    count2--;
                    if(count2 == 0)
                        type2 = -1;
                }
            }
            /*
cout << i << " --- " << endl;
cout << "type " << type << " -> " << count << " type2 " << type2
     << " -> " << count2 << endl;
                     */
        }
        return ans;
    }
};
/*
int main() {
    Solution s;
    vector<int> fruits = {1, 0, 3, 4, 3};
    cout << s.totalFruit(fruits) << endl;
}
*/