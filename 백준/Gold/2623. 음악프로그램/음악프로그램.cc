//음악 프로그램


#include<iostream>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<vector>
#include<queue>
#include<deque>


using namespace std;

int N, M;

vector<int> v[1005];
int deg[1005];
queue<int> q;

vector<int> arr;

void topology() {
	vector<int> result;
	for (int i = 1; i <= N; i++) {
		if (deg[i] == 0) {
			q.push(i);
		}
	}

	while (!q.empty()) {
		int now = q.front();
		q.pop();
		result.push_back(now);
		
		for (int nxt : v[now]) {
			deg[nxt]--;
			if (deg[nxt] == 0) {
				q.push(nxt);
			}
		}
	}

	if (result.size() == N) {
		for (int i = 0; i < N; i++) {
			cout << result[i] << "\n";
		}
	}
	else {
		cout << 0 << "\n";
	}
}




int main() {
	ios::sync_with_stdio(0);
	cout.tie(0);
	cin.tie(0);

	cin >> N >> M;

	int num = 0;
	for (int i = 0; i < M; i++) {
		cin >> num;
		arr.clear();
		int a;
		for (int j = 0; j < num; j++) {
			cin >> a;
			arr.push_back(a);
		}
		
		while (!arr.empty()) {
			int last = arr.back();
			arr.pop_back();
			for (int prev : arr) {
				v[prev].push_back(last);
				deg[last]++;
			}
		}

	}

	topology();

	return 0;
}