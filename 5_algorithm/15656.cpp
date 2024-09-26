#include <iostream>
#include <algorithm>
using namespace std;

int n, m;
int answer[7];

void permutation(int start, int num[], int depth) {
    if (depth == m) {
        for (int i = 0; i < m; i++)
            cout << answer[i] << ' ';
        cout << "\n";
        return;
    }
    for (int i = 0; i < n; i++) {
        answer[depth] = num[i];
        permutation(i + 1, num, depth + 1);
    }
}

int main(void) {
    cin >> n >> m;
    int num[n];
    for (int i = 0; i < n; i++)
        cin >> num[i];
    sort(num, num + n);
    permutation(0, num, 0);
}