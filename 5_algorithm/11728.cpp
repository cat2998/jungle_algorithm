#include <iostream>
using namespace std;

int main(void) {
    int n, m;

    cin >> n >> m;

    int a[n];
    int b[m];
    for (int i = 0; i < n; i++)
        cin >> a[i];
    for (int i = 0; i < m; i++)
        cin >> b[i];

    int i = 0, j = 0, x = 0;
    int ab[n + m];
    while (i < n && j < m) {
        if (a[i] <= b[j])
            ab[x++] = a[i++];
        else
            ab[x++] = b[j++];
    }
    while (i < n)
        ab[x++] = a[i++];
    while (j < m)
        ab[x++] = b[j++];

    for (int i = 0; i < n + m; i++)
        cout << ab[i] << ' ';
}