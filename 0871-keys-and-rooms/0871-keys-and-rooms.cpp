class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        
        int n = rooms.size();
        // hashmap to record whether a room has been visited/unlocked
        unordered_map<int,bool> visited;
        queue<int> q;
        
        // start from room 0
        visited[0] = true;
        q.push(0);
        int count = 1;  // number of rooms visited
        
        while (!q.empty()) {
            int room = q.front(); q.pop();
            // for each key in the current room
            for (int key : rooms[room]) {
                // if we haven't visited/unlocked it yet
                if (!visited[key]) {
                    visited[key] = true;
                    q.push(key);
                    count++;
                    // early exit if we've unlocked all rooms
                    if (count == n) return true;
                }
            }
        }
        
        // check if we managed to visit all rooms
        return count == n;

    }
};