//파이프 옮기기
// a형 기출

#include <iostream>
#include<cstring>
#include<algorithm>
#include<vector>
#include<queue>
#include<deque>


using namespace std;
int N;
int MAP[20][20];

int sy, sx, ey, ex ;

int dy[4] = { 0,1,1 };
int dx[4] = { 1,0,1 };

int total_cnt;

struct Pipe {
	int y, x, dir;
};

bool row_move(int ny1, int nx1) {
	if (ny1 < 0 || ny1 >= N || nx1 < 0 || nx1 >= N) {
		return false;
	}
	if (MAP[ny1][nx1] == 1)  return false;
	return true;
}

bool col_move(int ny2, int nx2) {
	if (ny2 < 0 || ny2 >= N || nx2 < 0 || nx2 >= N) {
		return false;
	}
	if (MAP[ny2][nx2] == 1)  return false;
	return true;
}

bool r_slash_move(int ny1, int nx1,int ny2, int nx2,int ny3, int nx3) {
	if (ny3 < 0 || ny3 >= N || nx3 < 0 || nx3 >= N) {
		return false;
	}
	if (ny2 < 0 || ny2 >= N || nx2 < 0 || nx2 >= N) {
		return false;
	}
	if (ny1 < 0 || ny1 >= N || nx1 < 0 || nx1 >= N) {
		return false;
	}
	if (MAP[ny3][nx3] == 1)  return false;
	if (MAP[ny2][nx2] == 1)  return false;
	if (MAP[ny1][nx1] == 1)  return false;
	return true;
}

void dfs(Pipe cp) {
	if (cp.y == ey && cp.x == ex) {
		total_cnt++;
		return;
	}

	int ny1 = cp.y + dy[0], nx1 = cp.x + dx[0];
	int ny2 = cp.y + dy[1], nx2 = cp.x + dx[1];
	int ny3 = cp.y + dy[2], nx3 = cp.x + dx[2];

	if (cp.dir == 0) {
		if (row_move(ny1, nx1)) {
			dfs({ ny1,nx1,0 });
		}
		if (r_slash_move(ny1, nx1, ny2, nx2, ny3, nx3)) {
			dfs({ ny3,nx3,2});
		}
	}
	else if (cp.dir == 1) {
		if (col_move(ny2, nx2)) {
			dfs({ ny2,nx2,1 });
		}
		if (r_slash_move(ny1, nx1, ny2, nx2, ny3, nx3)) {
			dfs({ ny3,nx3,2 });
		}
	}
	else if (cp.dir == 2) {
		if (row_move(ny1, nx1)) {
			dfs({ ny1,nx1 ,0});
		}
		if (col_move(ny2, nx2)) {
			dfs({ ny2,nx2 ,1});
		}
		if (r_slash_move(ny1, nx1, ny2, nx2, ny3, nx3)) {
			dfs({ ny3,nx3 ,2});
		}
	}
}


int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	cin >> N;
	sy = 0;
	sx = 1;
	ey = N - 1;
	ex = N - 1;
	int dir = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> MAP[i][j];
		}
	}

	dfs({ sy,sx,dir});

	cout << total_cnt << "\n";
	return 0;
}
