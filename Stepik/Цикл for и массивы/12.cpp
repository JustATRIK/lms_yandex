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
    cout << nums[n - 1] << " ";
    for (int i = 0; i < n - 1; i++) {
        cout << nums[i] << " ";
    }
    return 0;
}
