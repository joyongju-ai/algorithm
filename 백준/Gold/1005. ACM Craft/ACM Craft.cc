//백준 1005
//acmcraft


#include<iostream>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<vector>
#include<queue>
#include<deque>


using namespace std;

int N,K;
int delays[1005];
vector<int> v[1005];
int W;
int dp[1005];
int indegrees[1005];

void topology() {
	queue<int> q;
	for (int i = 1; i <= N; i++) {
		if (indegrees[i] == 0) {
			q.push(i);
			dp[i] = delays[i];
		}
	}

	while (!q.empty()) {
		int now = q.front();
		q.pop();
		if (now== W) {
			break;
		}
		for (int nxt : v[now]) {
			indegrees[nxt]--;
			dp[nxt] = max(dp[nxt], dp[now] + delays[nxt]);

			if (indegrees[nxt] == 0) {
				q.push(nxt);
			}
		}
	}

}



int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int T;
	cin >> T;

	for (int tc = 1; tc <= T; tc++) {
		memset(delays, 0, sizeof(delays));
		memset(dp, 0, sizeof(dp));
		memset(indegrees, 0, sizeof(indegrees));
		for (int i = 0; i < 1005; i++) {
			v[i].clear();
		}

		cin >> N >> K;
		
		for (int i = 1; i <= N; i++) {
			cin >> delays[i];
		}

		int pre, next;
		for (int i = 0; i < K; i++) {
			cin >> pre >> next;
			v[pre].push_back(next);
			indegrees[next]++;
		}
		cin >> W;

		topology();
		cout << dp[W] <<"\n";

	}
	

	return 0;
}