#include<iostream>
#include<vector>

using namespace std;

int main() {
    int n;
    int cn = 0;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int tmp;
        cin >> tmp;
        if (tmp > 0) {
            cn++;
        }
    }
    cout << cn;
    return 0;
}
