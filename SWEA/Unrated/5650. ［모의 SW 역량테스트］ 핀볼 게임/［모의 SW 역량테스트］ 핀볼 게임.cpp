//swea 5650
//핀볼 게임


#include<iostream>
#include<cstring>


using namespace std;

struct Wormhole {
	int y;
	int x;
	int num;
};

struct Pinball {
	int y;
	int x;
	int dir;
};

int map[105][105];
int dy[4] = { 0,1,0,-1 };
int dx[4] = { 1,0,-1,0 };
Wormhole wormholes[20];


void wormhole_move(int num, int& y,int &x, int wcnt) {
	for (int i = 0; i < wcnt; i++) {
		if (wormholes[i].num == num && (wormholes[i].y != y || wormholes[i].x != x)) {
			y = wormholes[i].y;
			x = wormholes[i].x;
			return;
		}
	}
}


int pinball_move(Pinball& pinball, int N,int wcnt) {
	int y = pinball.y;
	int x = pinball.x;
	int dir = pinball.dir;
	int point = 0;
	int moves = 0;
	while (true) {
		y = y + dy[dir];
		x = x + dx[dir];
		moves++;
		//벽
		if (x < 0 || x >= N || y < 0 || y >= N) {
			dir = (dir + 2) %4;
			point++;
			y = y + dy[dir];
			x = x + dx[dir];
		}
		//블록
		if (map[y][x] == 1) {
			if (dir == 0) {
				dir = (dir + 2) % 4;
			}
			else if (dir == 1) {
				dir = 0;
			}
			else if (dir == 2) {
				dir = 3;
			}
			else if (dir == 3) {
				dir = (dir + 2) % 4;
			}
			point++;
		}
		else if (map[y][x] == 2) {
			if (dir == 0) {
				dir = (dir + 2) % 4;
			}
			else if (dir == 1) {
				dir = (dir + 2) % 4;
			}
			else if (dir == 2) {
				dir = 1;
			}
			else if (dir == 3) {
				dir = 0;
			}
			point++;
		}
		else if (map[y][x] == 3) {
			if (dir == 0) {
				dir = 1;
			}
			else if (dir == 1) {
				dir = (dir + 2) % 4;
			}
			else if (dir == 2) {
				dir = (dir + 2) % 4;
			}
			else if (dir == 3) {
				dir = 2;
			}
			point++;
		}
		else if (map[y][x] == 4) {
			if (dir == 0) {
				dir = 3;
			}
			else if (dir == 1) {
				dir = 2;
			}
			else if (dir == 2) {
				dir = (dir + 2) % 4;
			}
			else if (dir == 3) {
				dir = (dir + 2) % 4;
			}
			point++;
		}
		else if (map[y][x] == 5) {
			dir = (dir + 2) % 4;
			point++;
		}
		// 웜홀
		else if (map[y][x] >= 6 && map[y][x] <= 10) {
			wormhole_move(map[y][x],y, x, wcnt);
		}
		//블랙홀
		else if (map[y][x] == -1) {
			return point;
		}
		//시작점 복귀
		if (moves != 0 && y == pinball.y && x == pinball.x) {
			return point;
		}
		
		
	}

}


int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T,N;
	int max_point = 0;
	int point = 0;
	cin >> T;
	for (int test_case = 1; test_case <= T; test_case++) {
		memset(wormholes, 0, sizeof(wormholes));//문제 발생 가능
		memset(map, 0, sizeof(map));
		max_point = 0;
		cin >> N;
		Wormhole wormhole;
		Pinball pinball;
		int wcnt = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				cin >> map[i][j];
				if (map[i][j] >= 6 && map[i][j] <= 10) {
					wormhole.y = i;
					wormhole.x = j;
					wormhole.num = map[i][j];
					wormholes[wcnt++] = wormhole;
				}
			}
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (map[i][j] == 0) {
					pinball.y = i;
					pinball.x = j;
					for (int dir = 0; dir < 4; dir++) {
						point = 0;
						pinball.dir = dir;
						point = pinball_move(pinball, N ,wcnt);
						if (max_point < point) {
							max_point = point;
						}
					}
				}
			}
		}
		cout << "#" << test_case << " " << max_point << endl;
	}
	return 0;
}