#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>

using namespace std;

int visited[21][21];
int visited_value[105];
int MAP[21][21];

int dx[4] = { 1,-1,-1,1 };
int dy[4] = { 1,1,-1,-1 };

int N;
int max_cnt;

struct Point {
	int y, x;
};

Point st;


void dfs(Point cp, int dir, int cost,int st_val, int rest_turn) {
	if (rest_turn < 0) {
		return;
	}
	if (cp.x == st.x && cp.y == st.y && cost > 0) {
		max_cnt = max(max_cnt, cost);
		//cout << cost << "#" << "\n";
		return;
	}


	for (int i = 0; i < 2; i++) {
		Point np = { cp.y + dy[(dir + i)%4], cp.x + dx[(dir + i)%4] };

		if (np.y < 0 || np.y >= N || np.x < 0 || np.x >= N) continue;
		if (visited_value[MAP[np.y][np.x]]) continue;
		if (visited[np.y][np.x]) continue;
		if (MAP[np.y][np.x] == st_val) {
			if (np.y != st.y || np.x != st.x) {
				continue;
			}
		}

		//cout << np.y << " " << np.x << "\n";
		visited[np.y][np.x] = 1;
		visited_value[MAP[np.y][np.x]] = 1;
		
		dfs(np, (dir + i)%4, cost + 1,st_val, rest_turn - i);
		visited[np.y][np.x] = 0;
		visited_value[MAP[np.y][np.x]] = 0;
		//cout << np.y << " " << np.x << "\n";
	}
}


int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T;
	cin >> T;

	for (int test_case = 1; test_case <= T; test_case++) {
		cin >> N;
		max_cnt = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				cin >> MAP[i][j];
			}
		}


		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				//cout << i <<" "<< j << "\n";
				st = { i,j };
				dfs(st, 0, 0, MAP[i][j],4);
				//cout << "\n";
			}
		}
		if (max_cnt == 0) cout << "#"<< test_case<<" "<< - 1 << "\n";
		else cout <<"#" << test_case <<" "<< max_cnt << "\n";
	}

	return 0;
}