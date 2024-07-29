#include <iostream>
using namespace std;

int main(void) {
    int n, d = 1;
    long sum = 0;

    cin >> n;

    char num[n];
    for (int i = 0; i < n; i++)
        cin >> num[i];

    for (int i = n - 1; i >= 0; i--) {
        if ('0' <= num[i] && num[i] <= '9') {
            sum += (num[i] - '0') * d;
            d *= 10;
        } else
            d = 1;
    }
    cout << sum;
}