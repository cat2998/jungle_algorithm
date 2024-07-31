#include <iostream>
using namespace std;

int k;
int answer[13];

void permutation(int arr[], int depth, int next) {
    if (depth == 6) {
        for (int i = 0; i < 6; i++)
            cout << answer[i] << ' ';
        cout << "\n";
        return;
    }
    for (int i = next; i < k; i++) {
        answer[depth] = arr[i];
        permutation(arr, depth + 1, i + 1);
    }
}

int main(void) {
    while (cin >> k && k != 0) {
        int arr[k];

        for (int i = 0; i < k; i++)
            cin >> arr[i];

        permutation(arr, 0, 0);
        cout << "\n";
    }
}