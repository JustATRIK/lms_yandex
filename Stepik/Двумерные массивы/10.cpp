#include <iostream>
using namespace std;

int main() {
    int n, m, k, r = 0;
    cin >> n >> m;
    int a[n][m];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> a[i][j];
        }
    }
    cin >> k;
    for (int i = 0; i < n; i++) {
        int near_free = 0;
        for (int j = 0; j < m; j++) {
            if (a[i][j] == 0) {
                near_free++;
                if (near_free == k) {
                    r = i + 1;
                    break;
                }
            }
            else near_free = 0;
        }
        if (near_free == k) break;
    }
    cout << r;
    return 0;
}