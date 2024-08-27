#include <iostream>
using namespace std;

void permutation(int n, int m, int visited[]) {
    for (int i = 1; i <= n; i++) {
        visited[i] = 1;
        for (int j = 1; j <= n; j++) {
            if (visited[j] == 0) {
                permutation
            }
        }
    }
}

int main(void) {
    int n, m;

    cin >> n >> m;

    int visited[n + 1];
    for (int i = 0; i < n + 1; i++)
        visited[i] = 0;

    permutation(n, m, visited);
}