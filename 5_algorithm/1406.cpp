#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main(void) {
    string s;
    int n;
    stack<char> left;
    stack<char> right;
    char cmd, x;

    cin >> s;
    cin >> n;

    for (int i = 0; i < s.size(); i++)
        left.push(s[i]);

    for (int i = 0; i < n; i++) {
        cin >> cmd;
        if (cmd == 'L') {
            if (!left.empty()) {
                right.push(left.top());
                left.pop();
            }
        } else if (cmd == 'D') {
            if (!right.empty()) {
                left.push(right.top());
                right.pop();
            }
        } else if (cmd == 'B') {
            if (!left.empty())
                left.pop();
        } else if (cmd == 'P') {
            cin >> x;
            left.push(x);
        }
    }

    while (!left.empty()) {
        right.push(left.top());
        left.pop();
    }

    while (!right.empty()) {
        cout << right.top();
        right.pop();
    }
}