#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
    int n, m, x;

    cin >> n;

    int card[n];
    for (int i = 0; i < n; i++)
        cin >> card[i];

    sort(card, card + n);

    cin >> m;
    for (int i = 0; i < m; i++) {
        scanf("%d", &x);
        int left = 0;
        int right = n - 1;
        int flag = 0;
        while (left <= right) {
            long mid = (left + right) / 2;
            if (card[mid] < x)
                left = mid + 1;
            else if (card[mid] > x)
                right = mid - 1;
            else {
                flag = 1;
                break;
            }
        }

        if (flag)
            cout << "1" << ' ';
        else
            cout << "0" << ' ';
    }
}