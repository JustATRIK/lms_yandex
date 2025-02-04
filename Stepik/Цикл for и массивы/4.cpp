#include<iostream>
#include<vector>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> nums = vector<int>();
    for (int i = 0; i < n; i++) {
        int tmp;
        cin >> tmp;
        if (tmp % 2 == 0) {
            nums.push_back(tmp);
        }
    }
    for (int i = 0; i < nums.size(); i++) {
        cout << nums[i] << " ";
    }
    return 0;
}
