#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool com(pair<int, int> a, pair<int, int> b) {
    if (a.first == b.first)
        return a.second < b.second;
    return a.first < b.first;
}

int main(void) {
    int n, a, b, answer = 1;

    cin >> n;

    int dp[n];
    vector<pair<int, int> > paper(n);
    for (int i = 0; i < n; i++) {
        cin >> a >> b;
        if (a < b)
            paper[i] = make_pair(a, b);
        else
            paper[i] = make_pair(b, a);
    }

    sort(paper.begin(), paper.end(), com);

    dp[0] = 1;
    for (int i = 1; i < n; i++) {
        dp[i] = 1;
        for (int j = 0; j < i; j++) {
            if (paper[j].second <= paper[i].second)
                dp[i] = max(dp[i], dp[j] + 1);
        }
        answer = max(answer, dp[i]);
    }

    cout << answer;
}
