#include <iostream>
using namespace std;

int n;
int answer[9] = {0};
int v[9] = {0};

void permutation(int depth) {
    if (depth == n) {
        for (int i = 0; i < depth; i++) {
            cout << answer[i] << ' ';
        }
        cout << "\n";
        return;
    }
    for (int i = 1; i <= n; i++) {
        if (v[i] == 0) {
            v[i] = 1;
            answer[depth] = i;
            permutation(depth + 1);
            v[i] = 0;
        }
    }
}

int main(void) {
    cin >> n;
    permutation(0);
}