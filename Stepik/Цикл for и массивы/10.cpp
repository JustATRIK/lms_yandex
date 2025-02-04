#include<iostream>
#include<vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> nums = vector<int>();
    for (int i = 0; i < n; i++) {
        int tmp;
        cin >> tmp;
        if (find(nums.begin(), nums.end(), tmp) == nums.end()) {
            nums.push_back(tmp);
        }
    }
    cout << nums.size();
    return 0;
}
