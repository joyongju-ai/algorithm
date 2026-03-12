#include<iostream>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<vector>
#include<unordered_map>
#include<set>

using namespace std;

long long  arr[1000005];
long long  seg[4000005];

int N, M, K;

long long  makeseg(int start,int end,int node) {
	if (start == end) {
		return seg[node] = arr[start];
	}
	
	int mid = (start+ end) / 2;

	return seg[node] = makeseg(start, mid, node * 2) + makeseg(mid + 1, end, node * 2 + 1);
}

long long query(int start, int end, int node, int ts, int te) {
	if (start > te || end < ts) {
		return 0;
	}

	if (start >= ts && end <= te) {
		return seg[node];
	}
	int mid = (start + end) / 2;

	return query(start, mid, node * 2, ts, te) + query(mid + 1, end, node * 2 + 1, ts, te);
	
}

long long update(int start, int end, int node, int index, long long val) {
	if (index < start || index > end) {
		return seg[node];
	}

	if (index == start && index == end) {
		seg[node] = val;
		return seg[node];
	}

	int mid = (start + end) / 2;

	return seg[node] = update(start, mid, node * 2, index, val) + update(mid + 1, end, node * 2 + 1, index, val);;
}


int main() {
	cin >> N >> M >> K;
	for (int i = 1; i <= N; i++) {
		cin >> arr[i];
	}
	makeseg(1, N, 1);

	long long a, b, c;
	for (int i = 0; i < M + K; i++) {
		cin >> a >> b >> c;
		if (a == 1) {
			update(1, N, 1, b, c);
		}
		else if (a == 2) {
			cout << query(1, N, 1, b, c)<<"\n";
		}
	}

	return 0;
}