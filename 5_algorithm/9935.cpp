#include <iostream>
#include <string>
#include <deque>
using namespace std;

int main(void) {
    int idx = 0;
    string sentence, bomb;
    deque<char> deque;

    cin >> sentence;
    cin >> bomb;

    while (true) {
        deque.push_back(sentence[idx++]);
        if (deque.size() >= bomb.size()) {
            int same = 1;
            for (int i = 0; i < bomb.size(); i++) {
                if (deque[deque.size() - 1 - i] != bomb[bomb.size() - 1 - i]) {
                    same = 0;
                    break;
                }
            }
            if (same) {
                for (int i = 0; i < bomb.size(); i++)
                    deque.pop_back();
            }
        }
        if (idx == sentence.size())
            break;
    }

    if (deque.size() == 0)
        cout << "FRULA";
    else {
        for (int i = 0; i < deque.size(); i++)
            cout << deque[i];
    }
}