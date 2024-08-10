#include <iostream>
using namespace std;

int n, m;
char map[101][101];
int cnt[101][101] = {0};

int dfs(int x, int y) {
    int num = 1;
    int dx[4] = {0, 0, 1, -1};
    int dy[4] = {1, -1, 0, 0};

    for (int i = 0; i < 4; i++) {
        int drx = dx[i] + x;
        int dry = dy[i] + y;
        if (0 <= drx && drx < n && 0 <= dry && dry < m) {
            if (map[x][y] == map[drx][dry] && cnt[drx][dry] == 0) {
                cnt[drx][dry] = 1;
                num += dfs(drx, dry);
            }
        }
    }

    return num;
}

int main(void) {
    string line;
    int num, my = 0, your = 0;

    cin >> m >> n;

    for (int i = 0; i < n; i++) {
        cin >> line;
        for (int j = 0; j < m; j++)
            map[i][j] = line[j];
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (cnt[i][j] == 0) {
                cnt[i][j] = 1;
                num = dfs(i, j);
                if (map[i][j] == 'W')
                    my += num * num;
                else
                    your += num * num;
            }
        }
    }

    cout << my << ' ' << your;
}