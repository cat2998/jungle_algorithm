#include <iostream>
using namespace std;

int n, m;
int visited[9] = {0};
int answer[8];

void permutation(int depth, int start) {
    if (depth == m) {
        for (int i = 0; i < m; i++)
            cout << answer[i] << ' ';
        cout << "\n";
        return;
    }
    for (int i = start; i <= n; i++) {
        if (visited[i] == 0) {
            answer[depth] = i;
            visited[i] = 1;
            permutation(depth + 1, i + 1);
            visited[i] = 0;
        }
    }
}

int main(void) {
    cin >> n >> m;
    permutation(0, 1);
}