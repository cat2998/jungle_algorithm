#include <iostream>
#include <vector>
#include <string>
#include <queue>
using namespace std;

int main(void) {
    int n;
    queue<int> que;

    cin >> n;
    cin.ignore();
    int time[n + 1];
    int answer[n + 1];
    vector<vector<int> > outdegree(n + 1);
    vector<vector<int> > indegree(n + 1);
    int indegree_cnt[n + 1];

    for (int i = 1; i < n + 1; i++)
        indegree_cnt[i] = 0;

    for (int i = 0; i < n; i++) {
        string str;
        getline(cin, str);
        int idx = 0;
        for (int j = 0; j < str.size(); j++) {
            if (str[j] == ' ') {
                if (idx == 0)
                    time[i + 1] = stoi(str.substr(idx, j - idx));
                else {
                    int m = stoi(str.substr(idx, j - idx));
                    outdegree[m].push_back(i + 1);
                    indegree[i + 1].push_back(m);
                    indegree_cnt[i + 1] += 1;
                }
                idx = j + 1;
            }
        }
    }

    for (int i = 1; i < n + 1; i++) {
        if (indegree_cnt[i] == 0)
            que.push(i);
    }

    while (!que.empty()) {
        int front = que.front();
        que.pop();
        int max = 0;
        for (int i = 0; i < indegree[front].size(); i++) {
            if (max < time[indegree[front][i]])
                max = time[indegree[front][i]];
        }
        time[front] += max;
        for (int i = 0; i < outdegree[front].size(); i++) {
            indegree_cnt[outdegree[front][i]]--;
            if (indegree_cnt[outdegree[front][i]] == 0)
                que.push(outdegree[front][i]);
        }
    }

    for (int i = 1; i < n + 1; i++)
        cout << time[i] << "\n";
}