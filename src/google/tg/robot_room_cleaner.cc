#include <bits/stdc++.h>
using namespace std;

// This is the robot's control interface.
// You should not implement it, or speculate about its implementation
class Robot {
  public:
    // Returns true if the cell in front is open and robot moves into the cell.
    // Returns false if the cell in front is blocked and robot stays in the
    // current cell.
    bool move();

    // Robot will stay in the same cell after calling turnLeft/turnRight.
    // Each turn will be 90 degrees.
    void turnLeft();
    void turnRight();

    // Clean the current cell.
    void clean();
};

class Solution {
  public:
    void cleanRoom(Robot &robot) {

        set<pair<int, int>> passed;
        unordered_map<int, pair<int, int>> delta;
        delta[0] = {-1, 0};
        delta[1] = {0, 1};
        delta[2] = {1, 0};
        delta[3] = {0, -1};
        rec(0, 0, 0, robot, delta, passed);
    }

    void rec(int r, int c, int direction, Robot &robot,
             unordered_map<int, pair<int, int>> &delta,
             set<pair<int, int>> &passed) {
        passed.insert({r, c});
        //cout << r << " " << c << endl;
        robot.clean();
        for(int i = 0; i < 4; i++) {
            int next_direction = (direction + i) % 4;
            int next_r = r + delta[next_direction].first;
            int next_c = c + delta[next_direction].second;
            if(passed.find({next_r, next_c}) == passed.end() && robot.move()) {
                rec(next_r, next_c, next_direction, robot, delta, passed);
                robot.turnRight();
                robot.turnRight();
                robot.move();
                robot.turnRight();
                robot.turnRight();
            }
            robot.turnRight();
        }
    }
};