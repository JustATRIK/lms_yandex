#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int a;
    cin >> a;
    int m[a][a];
    for (int i = 0; i < a; i++) {
        for (int j = 0; j < a; j++) {
            m[i][j] = (int) abs(i - j);
        }
    }
    for (int i = 0; i < a; i++) {
        for (int j = 0; j < a; j++) {
            cout << m[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}