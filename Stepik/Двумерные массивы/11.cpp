#include<iostream>
#include <iomanip>

using namespace std;

int main() {
    int a;
    int b;
    cin >> b >> a;
    int m[a][b];
    int m1[b][a];
    for (int i = 0; i < b; i++) {
        for (int j = 0; j < a; j++) {
            cin >> m1[i][j];
        }
    }
    for (int i = 0; i < b; i++) {
        for (int j = 0; j < a; j++) {
            m[j][b - i - 1] = m1[i][j];
        }
    }
    for (int i = 0; i < a; i++) {
        for (int j = 0; j < b; j++) {
             cout << m[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
