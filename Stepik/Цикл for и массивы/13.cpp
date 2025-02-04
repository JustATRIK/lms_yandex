#include<iostream>
#include<vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    int cn = 0;
    cin >> n;
    vector<int> nums = vector<int>(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (nums[i] == nums[j]) {
                cn++;
            }
        }
    }
    cout << cn;
    return 0;
}
