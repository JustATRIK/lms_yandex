#include<iostream>
#include<vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    int cn;
    cin >> n >> cn;
    vector<int> nums = vector<int>(n);
    for (int i = 0; i < cn; i++) {
        int s;
        int e;
        cin >> s >> e;
        s -= 1;
        for (int i = s; i < e; i++) {
            nums[i] = -1;
        }
    }
    for (int i = 0; i < n; i++) {
        if (nums[i] == -1) {
            cout << ".";
        } else {
            cout << "I";
        }
    }
    return 0;
}
