#include <iostream>

using namespace std;

int main() {
    int a;
    cin >> a;
    int m[a][a];
    for (int i = 0; i < a; i++) {
        for (int j = 0; j < a; j++) {
            if (i == j || i == a - 1 - j || i == a / 2 || j == a / 2) {
                m[i][j] = 1;
            } else {
                m[i][j] = 0;
            }
        }
    }
    for (int i = 0; i < a; i++) {
        for (int j = 0; j < a; j++) {
            if (m[i][j] == 0) {
                cout << "." << " ";
            } else {
                cout << "*" << " ";
            }
        }
        cout << endl;
    }
    return 0;
}