#include<iostream>
#include<vector>

using namespace std;

int main() {
    int n;
    int cn = 0;
    cin >> n;
    int min = 1e9;
    for (int i = 0; i < n; i++) {
        int tmp;
        cin >> tmp;
        if (tmp > 0 && tmp < min) {
            min = tmp;
        }
    }
    cout << min;
    return 0;
}
