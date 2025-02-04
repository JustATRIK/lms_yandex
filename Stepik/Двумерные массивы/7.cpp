#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int n;
    bool b;
    cin >> n;
    int m[n][n];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> m[i][j];
        }
    }
    b = true;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (m[i][j] != m[j][i]) {
                b = false;
            }
        }
    }
    if (b) {
        cout << "YES";
    } else {
        cout << "NO";
    }
    return 0;
}