//swea 5644
//무선충전


#include<iostream>
#include<cstring>
#include<algorithm>
#include<string>
#include<vector>

using namespace std;

struct Person_pos {
	int y;
	int x;
};

struct Bc {
	int y;
	int x;
	int c;
	int p;
};

int person_arr[11][11];
int bc_arr[8][11][11];
int person_moves[2][101];
int dx[5] = { 0 , 0, 1, 0, -1 };
int dy[5] = { 0, -1, 0, 1, 0 };

void bcs_arr_init(Bc bcs[8],int A) {
	for (int i = 0; i < A; i++) {
		for (int j = bcs[i].y - bcs[i].c; j <= bcs[i].y + bcs[i].c; j++) {
			for (int k = bcs[i].x - bcs[i].c; k <= bcs[i].x + bcs[i].c; k++) {
				if (j < 1 || j > 10 || k < 1 || k > 10) {
					continue;
				}
				if (abs(bcs[i].y - j) + abs(bcs[i].x - k) <= bcs[i].c) {
					bc_arr[i][j][k] = bcs[i].p;
				}
			}
		}
	}

}

void person_move(Person_pos &person1_pos, Person_pos &person2_pos, int i) {
	int person1_move = person_moves[0][i];
	int person2_move = person_moves[1][i];

	person1_pos.x += dx[person1_move];
	person1_pos.y += dy[person1_move];
	person2_pos.x += dx[person2_move];
	person2_pos.y += dy[person2_move];

}

int max_charge(Person_pos& person1_pos, Person_pos& person2_pos, int A) {
	int max_val = 0;
	int temp = 0;
	for (int i = 0; i < A; i++) {
		for (int j = 0; j < A; j++) {
			if ((i == j) && bc_arr[i][person1_pos.y][person1_pos.x] && bc_arr[j][person2_pos.y][person2_pos.x]) {
				temp = (bc_arr[i][person1_pos.y][person1_pos.x] + bc_arr[j][person2_pos.y][person2_pos.x])/2;
			}
			else {
				temp = bc_arr[i][person1_pos.y][person1_pos.x] + bc_arr[j][person2_pos.y][person2_pos.x];
			}
			if (temp > max_val) {
				max_val = temp;
			}
		}
	}
	return max_val;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T,M,A;
	cin >> T;
	int total = 0;
	for (int test_case = 1; test_case <= T; test_case++) {
		total = 0;
		memset(person_arr, 0, sizeof(person_arr));
		memset(bc_arr, 0, sizeof(bc_arr));
		memset(person_moves, -1, sizeof(person_moves));
		cin >> M >> A;

		Person_pos person1_pos = { 1,1 };
		Person_pos person2_pos = { 10,10 };
		
		Bc bcs[8];

		for (int i = 0; i < 2; i++) {
			for (int j = 0; j < M; j++) {
				cin >> person_moves[i][j];
			}
		}

		for (int i = 0; i < A; i++) {
			cin >> bcs[i].x >> bcs[i].y >> bcs[i].c >> bcs[i].p;
		}

		bcs_arr_init(bcs,A);
		total += max_charge(person1_pos, person2_pos, A); //초기 위치 충전량 갱신
		for (int i = 0; i < M; i++) {
			person_move(person1_pos, person2_pos,i);
			total += max_charge(person1_pos, person2_pos, A);
		}
		cout << "#" << test_case << " " << total << endl;
	}
	return 0;
}