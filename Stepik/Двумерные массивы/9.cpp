#include<iostream>
#include <iomanip>

using namespace std;

int main() {
    int a;
    int b;
    int k;
    int r = 0;
    cin >> b >> a;
    int m[b][a];
    int m1[a][b];
    for (int i = 0; i < b; i++) {
        for (int j = 0; j < a; j++) {
            cin >> m[i][j];
        }
    }
    for (int i = 0; i < b; i++) {
        for (int j = 0; j < a; j++) {
            m1[j][i] = m[i][j];
        }
    }
    for (int i = 0; i < a; i++) {
        for (int j = 0; j < b; j++) {
             cout << m1[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
