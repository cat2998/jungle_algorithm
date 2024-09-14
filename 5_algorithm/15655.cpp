#include <iostream>
#include <algorithm>
using namespace std;

int n, m;
int answer[8];

void permutation(int num[], int start, int depth) {
    if (depth == m) {
        for (int i = 0; i < m; i++)
            cout << answer[i] << ' ';
        cout << "\n";
        return;
    }
    for (int i = start; i < n; i++) {
        answer[depth] = num[i];
        permutation(num, i + 1, depth + 1);
    }
}

int main(void) {
    cin >> n >> m;
    int num[n];
    for (int i = 0; i < n; i++)
        cin >> num[i];
    sort(num, num + n);
    permutation(num, 0, 0);
}