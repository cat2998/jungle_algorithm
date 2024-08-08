#include <iostream>
using namespace std;

int main(void) {
    int n, x, answer = 0;

    cin >> n;

    int dp[n][n];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            cin >> dp[i][j];
            if (j == 0) {
                if (i != 0)
                    dp[i][j] = dp[i - 1][j] + dp[i][j];
            } else if (j == i)
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j];
            else
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + dp[i][j];
            if (answer < dp[i][j])
                answer = dp[i][j];
        }
    }

    cout << answer;
}