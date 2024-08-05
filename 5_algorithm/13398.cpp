#include <iostream>
using namespace std;

int main(void) {
    int n;

    cin >> n;

    int arr[n];
    int dp[n][2];
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    int ans = arr[0];
    for (int i = 0; i < n; i++) {
        dp[i][0] = dp[i][1] = arr[i];
        if (i == 0)
            continue;
        dp[i][0] = max(dp[i - 1][0] + arr[i], arr[i]);
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + arr[i]);
        ans = max(ans, max(dp[i][0], dp[i][1]));
    }
    cout << ans;
}