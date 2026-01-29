//swea 4013 특이한 자석
//개당 600만?

#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<deque>
#include<vector>
#include<cstring>

using namespace std;

struct Target_dir {
	int target;
	int dir;
};

void rotate(deque<int> &dq) {
	int last = dq.back();
	dq.pop_back();
	dq.push_front(last);
}

void rotate_reverse(deque<int>& dq) {
	int first = dq.front();
	dq.pop_front();
	dq.push_back(first);
}

int can_rotate(int right_val,int left_val,int dir) {
	if ((right_val + left_val) % 2) {
		return -dir;
	}
	return 0;
}

void rotate_setting(int target,const vector<deque<int>>&magnetics,int rotate_state[4]) {
	int nx = target - 1;
	int left_val, right_val;
	while (nx - 1 >= 0) {
		left_val = magnetics[nx - 1][2];
		right_val = magnetics[nx][6];
		rotate_state[nx - 1] = can_rotate(right_val, left_val, rotate_state[nx]);
		nx--;
	}
	nx = target - 1;
	while (nx + 1 < 4) {
		left_val = magnetics[nx][2];
		right_val = magnetics[nx + 1][6];
		rotate_state[nx + 1] = can_rotate(right_val, left_val, rotate_state[nx]);
		nx++;
	}
}
int main() {
	//freopen("sample_input.txt", "r", stdin);
	int top = 0;
	int result = 0;
	int T;
	cin >> T;
	ios::sync_with_stdio(0);
	cin.tie(0);
	for (int test_case = 1; test_case <= T; test_case++) {
		int K;
		int target;
		int dir;
		cin >> K;
		vector<deque<int>>magnetics(4);
		Target_dir target_dir;
		vector<Target_dir>target_dirs(K);
		int input;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 8; j++) {
				cin >> input;
				magnetics[i].push_back(input);
			}
		}
		//구조체 딥카피
		for (int i = 0; i < K; i++) {
			cin >> target_dir.target >> target_dir.dir;
			target_dirs[i] = target_dir;
		}
		for (int i = 0; i < K; i++) {
			int rotate_state[4] = { 0 };
			target = target_dirs[i].target;
			dir = target_dirs[i].dir;
			rotate_state[target - 1] = dir;
			rotate_setting(target, magnetics, rotate_state);
			for (int j = 0; j < 4; j++) {
				if (rotate_state[j] == 1) {
					rotate(magnetics[j]);
				}
				else if (rotate_state[j] == -1) {
					rotate_reverse(magnetics[j]);
				}
			}
		}
		result = magnetics[0][0] + magnetics[1][0] * 2 + magnetics[2][0] * 4 + magnetics[3][0] * 8;
		cout << "#" << test_case << " " << result<< endl;
	}
	



}