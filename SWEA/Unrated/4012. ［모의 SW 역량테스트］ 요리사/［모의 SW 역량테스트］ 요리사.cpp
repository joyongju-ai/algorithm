//조합으로 뽑고 싶었지만 불가능할 듯 하다.
//인덱스로 조절했었는데 그게 불가능해졌다.
// 음식 하나당 넣을까 말까 2개니까

#include<iostream>
#include<vector>
#include<cstring>
#include <cmath>
#include<algorithm>

using namespace std;

int S[20][20];
int A[20];
int B[20];


int min_gap = 1000000;

void B_init(int N) {
	memset(B, 0, sizeof(B));
	int cnt = 1;
	for (int i = 1; i <= N; i++) {
		int flag = 1;
		for (int j = 1; j <= N / 2; j++) {
			if (i == A[j]) {
				flag = 0;
				break;
			}
		}
		if (flag == 1) {
			B[cnt++] = i;
		}
	}
}

int cal_synergy_gap(int N) {
	int A_syn = 0;
	int B_syn = 0;
	int gap;
	for (int i = 1; i <= N / 2; i++) {
		for (int j = 1; j <= N / 2; j++) {
			if (i != j) {
				A_syn += S[A[i]][A[j]];
				B_syn += S[B[i]][B[j]];
			}
		}
	}
	gap = abs(A_syn - B_syn);
	return gap;
}


void cur(int lev, int next, int N) {
	if (lev == N / 2 +1) {
		B_init(N);
		int gap = cal_synergy_gap(N);
		min_gap = min(gap, min_gap);
		return;
	}

	for (int i = next; i <= N; i++) {
		A[lev] = i;
		cur(lev + 1, i+ 1, N);
		A[lev] = 0;
	}
}

int main(){

	ios::sync_with_stdio(0);
	cin.tie(0);

	int T;
	cin >> T;
	for (int test_case = 1; test_case <= T; test_case++) {
		min_gap = 1000000;
		memset(S, 0, sizeof(S));
		memset(A, 0, sizeof(A));
		memset(B, 0, sizeof(B));

		int N;
		cin >> N;

		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				cin >> S[i][j];
			}
		}

		cur(1, 1, N);
		cout << "#" << test_case << " " << min_gap << endl;
	}
	return 0;
}