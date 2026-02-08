//swea 1949
//등산로 조성


#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>

using namespace std;

int N, K;
int map[10][10];
int visited[10][10];
int dy[4] = { 0,1,0,-1 };
int dx[4] = { 1,0,-1,0 };
int max_length;

struct Point {
	int y, x;
};

Point sts[5];

void dfs(Point cp, int lev) {
	max_length = max(max_length, lev);
	//cout << cp.y << " " << cp.x << "\n";
	for (int i = 0; i < 4; i++) {
		Point np = { cp.y + dy[i],cp.x + dx[i] };

		if (np.y < 0 || np.y >= N || np.x < 0 || np.x >= N) continue;
		if (visited[np.y][np.x]) continue;
		if (map[np.y][np.x] >= map[cp.y][cp.x]) continue;

		//cout << np.y << " " << np.x << "\n";
		visited[np.y][np.x] = 1;
		dfs(np, lev + 1);
		visited[np.y][np.x] = 0;

	}

}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T;
	cin >> T;
	for (int test_case = 1; test_case <= T; test_case++) {
		memset(map, 0, sizeof(map));
		memset(sts, 0, sizeof(sts));
		memset(visited, 0, sizeof(visited));
		cin >> N >> K;
		max_length = 0;

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				cin >> map[i][j];
			}
		}

		int max_val = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				max_val = max(max_val, map[i][j]);
			}
		}

		int cnt = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (map[i][j] == max_val) {
					sts[cnt++] = { i,j };
				}
			}
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				for (int depth = 1; depth <= K; depth++) {
					map[i][j] -= depth;
					for (int k = 0; k < cnt; k++) {
						if (sts[k].y == i && sts[k].x == j) continue;
						visited[sts[k].y][sts[k].x] = 1;
						dfs(sts[k], 1);
						memset(visited, 0, sizeof(visited));
					}
					map[i][j] += depth;
				}
			}
		}
		cout << "#" << test_case << " " << max_length << "\n";
	}
	return 0;
}

