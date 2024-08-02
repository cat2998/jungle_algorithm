#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
    int k, n;
    long left = 1;
    long right;
    long result;

    cin >> k >> n;

    int line[k];
    for (int i = 0; i < k; i++)
        cin >> line[i];

    sort(line, line + k);
    right = line[k - 1];
    result = left;

    while (left <= right) {
        int sum = 0;
        long mid = (left + right) / 2;
        for (int i = 0; i < k; i++) {
            sum += line[i] / mid;
        }
        cout << "left: " << left << "\n";
        cout << "mid: " << mid << "\n";
        cout << "right: " << right << "\n";
        cout << "sum: " << sum << "\n\n";
        if (sum >= n) {
            left = mid + 1;
            if (sum == n && result < mid)
                result = mid;
        } else if (sum < n)
            right = mid - 1;
    }

    cout << right;
}