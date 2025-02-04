#include <iostream>

using namespace std;

int main() {
    int a;
    int b;
    int x;
    int y;
    int tmp;
    cin >> a >> b;
    int m[a][b];
    for (int i = 0; i < a; i++) {
        for (int j = 0; j < b; j++) {
            cin >> m[i][j];
        }
    }
    cin >> x >> y;
    for (int i = 0; i < a; i++) {
        tmp = m[i][x];
        m[i][x] = m[i][y];
        m[i][y] = tmp;
    }
    for (int i = 0; i < a; i++) {
        for (int j = 0; j < b; j++) {
            cout << m[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}