#include<iostream>
#include<vector>

using namespace std;

int main() {
    int n;
    int cn = 0;
    cin >> n;
    int old;
    cin >> old;
    for (int i = 0; i < n - 1; i++) {
        int tmp;
        cin >> tmp;
        if (tmp > old) {
            cout << tmp << " ";
        }
        old = tmp;
    }
    return 0;
}
