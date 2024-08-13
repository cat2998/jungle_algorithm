#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
    int n, k;

    cin >> n >> k;

    int coin[n];
    int dp[k + 1];
    for (int i = 0; i < n; i++)
        cin >> coin[i];

    for (int i = 0; i < k + 1; i++)
        dp[i] = 0;
    dp[0] = 1;
    sort(coin, coin + n);

    for (int i = 0; i < n; i++) {
        for (int j = coin[i]; j <= k; j++) {
            dp[j] += dp[j - coin[i]];
        }
    }

    cout << dp[k];
}