#include<iostream>
#include<vector>

using namespace std;

int main() {
    int n;
    cin >> n;
    int min = 0;
    for (int i = 0; i < n; i++) {
        int tmp;
        cin >> tmp;
        if (tmp % 2 != 0 && (tmp < min || min == 0)) {
            min = tmp;
        }
    }
    cout << min;
    return 0;
}
