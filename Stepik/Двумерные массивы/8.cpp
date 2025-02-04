#include<iostream>
#include <iomanip>

using namespace std;

int main() {
    int b;
    int k;
    cin >> b;
    int m[b][b];
    for (int i = 0; i < b; i++) {
        for (int j = 0; j < b; j++) {
            cin >> m[i][j];
        }
    }
    cin >> k;
    for (int i = 0; i < b; i++) {
        for (int j = 0; j < b; j++) {
            if (i - j - k == 0) {
                cout << m[i][j] << " ";
            }
        }
    }
    return 0;
}
