#include <iostream>
using namespace std;

int main(void) {
    int n, k;

    cin >> n >> k;
    long dp[k + 1][n + 1];
    for (int i = 1; i <= k; i++) {
        for (int j = 1; j <= n; j++) {
            if (i == 1)
                dp[i][j] = j;
            else if (i * 2 > j)
                dp[i][j] = 0;
            else if (i * 2 == j)
                dp[i][j] = 2;
            else
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j - 2]) % 1000000003;
        }
    }

    cout << dp[k][n] % 1000000003;
}