#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool compare(pair<int, int> a, pair<int, int> b) {
    return a.first < b.first;
}

int main(void) {
    int n, l, x, y, start, answer = 0;

    cin >> n >> l;

    vector<pair<int, int> > water(n);
    for (int i = 0; i < n; i++) {
        cin >> x >> y;
        water[i] = make_pair(x, y);
    }

    sort(water.begin(), water.end(), compare);

    start = water[0].first;
    for (int i = 0; i < n; i++) {
        x = water[i].first;
        y = water[i].second;
        if (x < start)
            x = start;
        while (x < y) {
            x += l;
            answer++;
        }
        start = x;
    }

    cout << answer;
}
