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
    for (int i = 0; i < n - n % 2 - 1; i += 2) {
        cout << nums[i + 1] << " " << nums[i] << " ";
    }
    if (n % 2 == 1) {
        cout << nums[n - 1];
    }
    return 0;
}
