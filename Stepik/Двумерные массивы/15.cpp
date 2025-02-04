#include <iostream>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    int a[n+2][m+2];

    for (int i = 0; i <= n + 1; i++) {
        for (int j = 0; j <= m + 1; j++) {
            a[i][j] = -1;
        }
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            a[i][j] = 0;
        }
    }
    int num = 0, row = 1, col = 0;

    while (num < n * m) {
        while (a[row][col + 1] == 0) {
            col++;
            num++;
            a[row][col] = num;
        }
        while (a[row + 1][col] == 0) {
            row++;
            num++;
            a[row][col] = num;
        }
        while (a[row][col - 1] == 0) {
            col--;
            num++;
            a[row][col] = num;
        }
        while (a[row - 1][col] == 0) {
            row--;
            num++;
            a[row][col] = num;
        }
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (a[i][j] % 10 == a[i][j]) cout << "   ";
            else if (a[i][j] % 100 == a[i][j]) cout << "  ";
            else if (a[i][j] % 1000 == a[i][j]) cout << " ";
            cout << a[i][j];
        }
        cout << endl;
    }
    return 0;
}