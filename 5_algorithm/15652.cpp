#include <iostream>
using namespace std;

int n, m;
int visited[9] = {0};
int answer[8];

void permutation(int start, int depth) {
    if (depth == m) {
        for (int i = 0; i < m; i++)
            cout << answer[i] << ' ';
        cout << "\n";
        return;
    }
    for (int i = start; i <= n; i++) {
        answer[depth] = i;
        permutation(i, depth + 1);
    }
}

int main(void) {
    cin >> n >> m;
    permutation(1, 0);
}