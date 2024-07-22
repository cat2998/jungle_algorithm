#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void) {
    int a_num, b_num;
    int i, j, cnt;

    cin >> a_num >> b_num;

    vector<int> a(a_num);
    vector<int> b(b_num);

    for (int i = 0; i < a_num; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < b_num; i++) {
        cin >> b[i];
    }

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    i = j = cnt = 0;
    while (i < a_num || j < b_num) {
        if (i < a_num && j < b_num) {
            if (a[i] == b[j]) {
                i++;
                j++;
            } else if (a[i] < b[j]) {
                cnt++;
                i++;
            } else {
                cnt++;
                j++;
            }
        } else {
            cnt++;
            i++;
            j++;
        }
    }

    cout << cnt;
}