#include <iostream>
#include <algorithm>
using namespace std;

int n, m;
int answer[8];

void permutation(int num[], int visited[], int depth) {
    if (depth == m) {
        for (int i = 0; i < m; i++)
            cout << answer[i] << ' ';
        cout << "\n";
        return;
    }
    for (int i = 0; i < n; i++) {
        if (visited[i] == 0) {
            visited[i] = 1;
            answer[depth] = num[i];
            permutation(num, visited, depth + 1);
            visited[i] = 0;
        }
    }
}

int main(void) {
    cin >> n >> m;

    int num[n];
    int visited[n];
    for (int i = 0; i < n; i++) {
        cin >> num[i];
        visited[i] = 0;
    }

    sort(num, num + n);

    permutation(num, visited, 0);
}