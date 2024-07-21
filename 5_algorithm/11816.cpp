#include <iostream>
using namespace std;

int main(void) {
    string n;
    cin >> n;

    int len = n.length();
    int sum = 0;

    if (len > 2 && n[0] == '0' && n[1] == 'x') {
        for (int i = len - 1; i > 1; i--) {
            if (0 <= n[i] - '0' && n[i] - '0' <= 9)
                sum += (n[i] - '0') * pow(16, len - i - 1);
            else
                sum += (n[i] - 'a' + 10) * pow(16, len - i - 1);
        }
    } else if (len > 1 && n[0] == '0') {
        for (int i = len - 1; i > 0; i--) {
            sum += (n[i] - '0') * pow(8, len - i - 1);
        }
    } else {
        sum = stoi(n);
    }
    cout << sum;
}