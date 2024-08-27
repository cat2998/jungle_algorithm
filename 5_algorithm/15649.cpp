#include <iostream>
using namespace std;

int n, m;
int answer[8];
int visited[9] = {0};

void permutation(int depth) {
    if (depth == m) {
        for (int i = 0; i < m; i++) {
            cout << answer[i] << ' ';
        }
        cout << "\n";
        return;
    }
    for (int i = 1; i <= n; i++) {
        if (visited[i] == 0) {
            answer[depth] = i;
            visited[i] = 1;
            permutation(depth + 1);
            visited[i] = 0;
        }
    }
}

int main(void) {
    cin >> n >> m;
    permutation(0);
}