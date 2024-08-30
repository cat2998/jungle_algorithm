#include <iostream>
using namespace std;

int n, m;
int answer[8];

void permutation(int depth) {
    if (depth == m) {
        for (int i = 0; i < m; i++)
            cout << answer[i] << ' ';
        cout << "\n";
        return;
    }
    for (int i = 1; i <= n; i++) {
        answer[depth] = i;
        permutation(depth + 1);
    }
}

int main(void) {
    cin >> n >> m;
    permutation(0);
}