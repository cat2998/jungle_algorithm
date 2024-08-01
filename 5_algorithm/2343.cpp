#include <iostream>
using namespace std;

int main(void) {
    int n, m;
    int start = 0;
    long end;

    cin >> n >> m;

    int lesson[n];
    for (int i = 0; i < n; i++) {
        cin >> lesson[i];
        end += lesson[i];
        if (start < lesson[i])
            start = lesson[i];
    }

    while (start < end) {
        long middle = (start + end) / 2;
        int sum = 0;
        int cnt = 1;

        for (int i = 0; i < n; i++) {
            sum += lesson[i];
            if (sum > middle) {
                cnt++;
                sum = lesson[i];
            }
        }

        if (cnt <= m)
            end = middle;
        else if (cnt > m)
            start = middle + 1;
    }

    cout << end;
}