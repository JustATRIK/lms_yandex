#include<iostream>
#include<vector>
#include <algorithm>

using namespace std;

int main() {
    vector<int> nums = vector<int>(8);
    for (int i = 0; i < 8; i++) {
        int s;
        int e;
        cin >> s >> e;
        nums[i] = s * 10 + e;
    }
    for (int i = 0; i < 8; i++) {
        int x1 = nums[i] / 10;
        int y1 = nums[i] % 10;
        for (int j = i + 1; j < 8; j++) {
            int x2 = nums[j] / 10;
            int y2 = nums[j] % 10;
            if (x2 == x1 || y1 == y2 || x1 - y1 == x2 - y2 || x1 + y1 == x2 + y2) {
                cout << "YES";
                return 0;
            }
        }
    }
    cout << "NO";
    return 0;
}
