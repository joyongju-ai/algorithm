//swea 5648
//원자소멸 시뮬레이션


#include<iostream>
#include<cstring>
#include<algorithm>

using namespace std;

struct Atom {
	int y;
	int x;
	int dir;
	int K;
};

int dx[4] = { 0,0,-1,1 };
int dy[4] = { 1,-1,0,0 };

Atom atoms[1001];

//int arr[4000][4000] = { 0 };
int meet[4001][4001] = { 0 };
//기존 좌표의 에너지를 배열 arr에서 지우고 새로운 위치의 에너지를 배열 arr에 넣기
void atom_move(int N) {
	for (int i = 0; i < N; i++) {
		if (atoms[i].x < 0 || atoms[i].x > 4000 || atoms[i].y < 0 || atoms[i].y > 4000) {
			continue;
		}
		meet[atoms[i].y][atoms[i].x] = -1;
		if (!atoms[i].K) {
			continue;
		}
		atoms[i].y += dy[atoms[i].dir];
		atoms[i].x += dx[atoms[i].dir];
	}
}
//
int atom_meet(int N) {
	int energy = 0;
	for (int i = 0; i < N; i++) {
		if (!atoms[i].K) {
			continue;
		}
		if (atoms[i].x < 0 || atoms[i].x > 4000 || atoms[i].y < 0 || atoms[i].y > 4000) {
			continue;
		}
		if (meet[atoms[i].y][atoms[i].x] != -1) {
			energy += atoms[meet[atoms[i].y][atoms[i].x]].K;
			energy += atoms[i].K;
			atoms[meet[atoms[i].y][atoms[i].x]].K = 0;
			atoms[i].K = 0;
			meet[atoms[i].y][atoms[i].x] = i;
		}
		else {
			meet[atoms[i].y][atoms[i].x] = i;
		}
	}
	return energy;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int T;
	int N, total;
	cin >> T;

	for (int test_case = 1; test_case <= T; test_case++) {
		memset(atoms, 0, sizeof(atoms));
		memset(meet, -1, sizeof(meet));
		//memset(arr, 0, sizeof(arr));
		total = 0;
		cin >> N;
		for (int i = 0; i < N; i++) {
			cin >> atoms[i].x >> atoms[i].y >> atoms[i].dir >> atoms[i].K;
			atoms[i].y *= 2;
			atoms[i].x *= 2;
			atoms[i].y += 2000;
			atoms[i].x += 2000;
		}
		for (int moves = 0; moves < 4000; moves++) {
			atom_move(N);
			total += atom_meet(N);
		}
		cout << "#" << test_case << " " << total << endl;
	}
	return 0;
}