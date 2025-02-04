#include<iostream>
#include <iomanip>

using namespace std;

int main() {
    int a;
    int b;
    cin >> a >> b;
    int m[a][b];
    int p = 0;
    int r = 0;
    int c = 0;
    int n = 1;
    for (int mi = 0; mi < a; mi++) {
        c = p - 1;
        for (p = c; p < b; p++) {
            r = mi;
            for (int j = p; j >= 0; j--) {
                if (r < a) {
                    m[r][j] = n;
                    n++;
                    r++;
                } else {
                    break;
                }
            }
        }
    }
    for (int i = 0; i < a; i++) {
        for (int j = 0; j < b; j++) {
             cout << setw(4) << m[i][j];
        }
        cout << endl;
    }
    return 0;
}
