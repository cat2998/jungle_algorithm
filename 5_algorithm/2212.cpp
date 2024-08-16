#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
    int n, k, answer = 0;

    cin >> n >> k;

    int sencor[n];
    int distance[n - 1];

    for (int i = 0; i < n; i++)
        cin >> sencor[i];

    sort(sencor, sencor + n);

    for (int i = 0; i < n - 1; i++)
        distance[i] = sencor[i + 1] - sencor[i];

    sort(distance, distance + n - 1);

    for (int i = 0; i < n - k; i++)
        answer += distance[i];

    cout << answer;
}