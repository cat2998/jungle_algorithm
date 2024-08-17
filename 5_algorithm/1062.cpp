#include <iostream>
#include <string>
#include <map>
using namespace std;

bool compare(pair<char, int> a, pair<char, int> b) {
    return a.second >= b.second;
}

int main(void) {
    int n, k, answer = 0;
    map<char, int> m;

    cin >> n >> k;

    string sentence[n];
    for (int i = 0; i < n; i++) {
        cin >> sentence[i];
        for (int j = 4; j < sentence[i].size() - 4; j++) {
            m[sentence[i][j]]++;
        }
    }

    if (k <= 5) {
        cout << answer;
        return 0;
    }

    sort(m.begin(), m.end(), compare);

    for (auto itr : m) {
        cout << itr.first << ' ' << itr.second << "\n";
    }
}