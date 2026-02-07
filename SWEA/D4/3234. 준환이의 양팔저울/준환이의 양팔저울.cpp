// 준환이의 양팔저울
// swea 3234

#include<iostream>
#include<cstring>
#include<string>
#include<algorithm>
#include<cmath>

using namespace std;


int N;
int weight[15];
int visited[15];
int cnt;
int total;
int dL[2] = { 1, 0};
int dR[2] = { 0, 1};
int factorial[] = { 0, 1,2,6,24,120,720,5040,40320,362880,3628800 };
int power[] = { 1,2,4,8,16,32,64,128,256,512,1024 };
void dfs(int lev, int left, int right) {
	if (lev == N) {
		cnt++;
		//cout << cnt << endl;
		return;
	}
	if (left  > (total / 2)) {
		int result = power[N - lev];
		result *= factorial[N - lev];
		cnt += result;
		return;
	}
	for (int i = 0; i < N; i++) {
		for (int dir = 0; dir < 2; dir++) {
			if (!visited[i]) {
				if (left + dL[dir]*weight[i] >= right + dR[dir]* weight[i]) {	
					visited[i] = 1;
					dfs(lev + 1, left + dL[dir] * weight[i], right + dR[dir] * weight[i]);
					visited[i] = 0;
				}
			}
		}
	}
}



int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int T;
	cin >> T;

	for (int test_case = 1; test_case <= T; test_case++) {
		memset(weight, 0, sizeof(weight));
		memset(visited, 0, sizeof(visited));

		cnt = 0;
		total = 0;
		cin >> N;
		for (int i = 0; i < N; i++) {
			cin >> weight[i];
			total += weight[i];
		}
		//cout << total;
		dfs(0, 0, 0);
		cout << "#" << test_case <<" "<<cnt << "\n";
	}
	
	return 0;
}