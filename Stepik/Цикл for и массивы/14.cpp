#include<iostream>
#include<vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> nums = vector<int>(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    for (int i = 0; i < n; i++) {
        if (count(nums.begin(), nums.end(), nums[i]) == 1) {
            cout << nums[i] << " ";
        }
    }
    return 0;
}