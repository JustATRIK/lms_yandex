#include<iostream>
#include<vector>

using namespace std;

int main() {
    int n;
    int cn = 0;
    cin >> n;
    long old;
    cin >> old;
    for (int i = 0; i < n - 1; i++) {
        long tmp;
        cin >> tmp;
        if (tmp * old > 0) {
            if (old > tmp) {
                cout << tmp << " " << old;
            } else {
                cout << old << " " << tmp;
            }
            break;
        }
        old = tmp;
    }
    return 0;
}
