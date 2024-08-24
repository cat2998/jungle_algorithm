#include <iostream>
#include <string>
using namespace std;

int answer = 0;
bool alphabet[26] = {false};

void permutation(string sentence[], int n, int start, int k) {
    if (k == 0) {
        int cnt = 0;
        // for (int i = 0; i < 26; i++) {
        //     cout << i << ": " << alphabet[i] << "\n";
        // }
        for (int i = 0; i < n; i++) {
            int flag = 0;
            for (int j = 0; j < sentence[i].size(); j++) {
                if (!alphabet[sentence[i][j] - 'a']) {
                    flag = 1;
                    break;
                }
            }
            if (flag == 0)
                cnt++;
        }
        if (answer < cnt)
            answer = cnt;
    }
    for (int i = start; i < 26; i++) {
        if (!alphabet[i]) {
            alphabet[i] = true;
            permutation(sentence, n, i + 1, k - 1);
            alphabet[i] = false;
        }
    }
}

int main(void) {
    int n, k;

    cin >> n >> k;

    string sentence[n];
    for (int i = 0; i < n; i++)
        cin >> sentence[i];

    if (k < 5) {
        cout << answer;
        return 0;
    }

    k -= 5;
    alphabet['a' - 'a'] = true;
    alphabet['n' - 'a'] = true;
    alphabet['t' - 'a'] = true;
    alphabet['i' - 'a'] = true;
    alphabet['c' - 'a'] = true;

    permutation(sentence, n, 0, k);

    cout << answer;
}