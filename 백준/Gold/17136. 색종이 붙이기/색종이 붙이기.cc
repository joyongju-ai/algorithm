//색종이 붙이기 a형 기출

#include<iostream>
#include<cstring>
#include<algorithm>
#include<vector>
#include<queue>
#include<deque>
#include<cmath>


using namespace std;
int MAP[15][15];
int papers[6];
int min_cost = 21e8;

bool paper_check(int y, int x,int paper_size) {
	if (y + paper_size - 1 >= 10 || x + paper_size - 1 >= 10) {
		return false;
	}
	for (int r = 0; r < paper_size; r++) {
		for (int c = 0; c < paper_size; c++) {
			if (MAP[y + r][x + c] == 0) {
				return false;
			}
		}
	}
	return true;
}

bool is_valid() {
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 10; j++) {
			if (MAP[i][j] == 1) {
				return false;
			}
		}
	}
	return true;
}


void dfs(int y, int x, int cost) {
	if (y == 10 && x == 10) {
		if (is_valid()) {
			min_cost = min(cost, min_cost);
		}
		return;
	}

	for (int i = 1; i <= 5; i++) {
		if (papers[i] == 0) continue;
		if (!paper_check(y,x,i)) continue; 

		for (int r = 0; r < i; r++) {
			for (int c = 0; c < i; c++) {
				MAP[y + r][x + c] = 0;
			}
		}

		papers[i]--;

		int ny = 10, nx = 10;
		int flag = 0;
		for (int r = y; r < 10; r++) {
			for (int c = 0; c < 10; c++) {
				if (MAP[r][c] == 1) {
					ny = r;
					nx = c;
					flag = 1;
					break;
				}
			}
			if (flag == 1) {
				break;
			}
		}

		dfs(ny, nx,cost + 1);

		for (int r = 0; r < i; r++) {
			for (int c = 0; c < i; c++) {
				MAP[y + r][x + c] = 1;
			}
		}
		papers[i]++;
	}
}

int main() {
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 10; j++) {
			cin >> MAP[i][j];
		}
	}
	
	for (int i = 1; i <= 5; i++) {
		papers[i] = 5;
	}

	int y = 0;
	int x = 0;
	int flag = 0;
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 10; j++) {
			if (MAP[i][j] == 1) {
				flag = 1;
				y = i;
				x = j;
				break;
			}
		}
		if (flag == 1) {
			break;
		}
	}
	if (flag == 1) {
		dfs(y, x, 0);
	}
	else {
		min_cost = 0;
	}

	if (min_cost == 21e8) {
		cout << -1 << "\n";
	}
	else {
		cout << min_cost << "\n";
	}

	return 0;
}