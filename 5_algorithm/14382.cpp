#include <iostream>
using namespace std;

int main(void) {
    int t;
    long n;

    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> n;
        int number[10] = {0};
        if (n == 0)
            cout << "Case #" << i + 1 << ": INSOMNIA\n";
        else {
            int m = 2;
            int origin = n;
            while (true) {
                int sum = 0;
                string str = to_string(n);
                for (int j = 0; j < str.size(); j++) {
                    number[str[j] - '0'] = 1;
                }
                for (int j = 0; j < 10; j++) {
                    sum += number[j];
                }
                if (sum == 10) {
                    cout << "Case #" << i + 1 << ": " << n <<"\n";
                    break;
                }
                n = m * origin;
                m++;
            }
        }
    }
}