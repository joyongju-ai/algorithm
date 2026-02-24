//백준 2637
//장난감 조립

#include<iostream>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<vector>
#include<queue>
#include<deque>


using namespace std;


int N, M;
struct Part {
	int num, count;
};

vector<int> v[105];

int memo[105][105];//memo[i][j] i부품을 만드는데 필요한 j부품 개수
vector<int> basics;
int indegrees[105];

void topology() {
	queue<int> q;
	for (int i = 1; i <= N; i++) {
		if (indegrees[i] == 0) {
			q.push(i);
			basics.push_back(i);
			memo[i][i] = 1;
		}
	}

	while (!q.empty()) {
		int now = q.front();
		q.pop();

		for (int nxt : v[now]) {
			indegrees[nxt]--;
			for (int basic : basics) {
				if (now != basic) {
					memo[nxt][basic] += memo[nxt][now] * memo[now][basic];
				}
			}
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

	cin >> N >> M;

	int pre, next,count;
	for (int i = 0; i < M; i++) {
		cin >> next >> pre >> count;
		v[pre].push_back(next);
		indegrees[next]++;
		memo[next][pre] = count;
	}

	topology();
	for (int basic : basics) {
		cout << basic << " " << memo[N][basic] << "\n";
	}

	return 0;
}
