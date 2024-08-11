#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main(void) {
    int n, m, a, b, cnt = 0;
    queue<int> que;

    cin >> n;
    cin >> m;

    vector<vector<int> > computer(n + 1);
    int v[n + 1];
    for (int i = 0; i < m; i++) {
        cin >> a >> b;
        computer[a].push_back(b);
        computer[b].push_back(a);
        v[a] = 0;
        v[b] = 0;
    }

    que.push(1);
    v[1] = 1;
    while (!que.empty()) {
        int x = que.front();
        que.pop();
        cnt++;
        for (int i = 0; i < computer[x].size(); i++) {
            if (v[computer[x][i]] == 0) {
                v[computer[x][i]] = 1;
                que.push(computer[x][i]);
            }
        }
    }

    cout << cnt - 1;
}