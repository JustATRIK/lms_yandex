#include<iostream>
#include <iomanip>

using namespace std;

int main() {
    int a;
    int b;
    cin >> a >> b;
    int m[a][b];
    int c = 1;
    for (int i = 0; i < a; i++) {
        for (int j = 0; j < b; j++) {
            if ((i % 2 == 0 && j % 2 == 0) || (i % 2 != 0 && j % 2 != 0)) {
                m[i][j] = c++;
            } else {
                m[i][j] = 0;
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
