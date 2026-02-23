//계보복원가 호석
// https://www.acmicpc.net/problem/21276


#include<iostream>
#include<cstring>
#include<vector>
#include<algorithm>
#include<cmath>
#include<queue>
#include<deque>
#include<unordered_map>

using namespace std;

vector<int> v[1005];
vector<string>v_str[1005];
int pre[1005];
int N, M;

struct compare {
	bool operator()(const string& a, const string& b) {
		return a > b;
	}
};

priority_queue<string,vector<string>,compare> ordered_names;
vector<string> roots;

unordered_map<string, int> name_num;
unordered_map<int,string> num_name;


void topology() {
	queue<int> q;
	int cnt = 0;
	for (int i = 0; i < N; i++) {
		if (pre[i] == 0) {
			cnt++;
			q.push(i);
		}
	}

	while (!q.empty()) {
		int now = q.front();
		q.pop();
		if (cnt > 0) {
			cnt--;
			roots.push_back(num_name[now]);
		}
		
		ordered_names.push(num_name[now]);
		

		for (int nxt : v[now]) {
			pre[nxt]--;
			if (pre[nxt] == 0) {
				q.push(nxt);
			}
		}
	}

}


int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	cin >> N;
	string name;
	for (int i = 0; i < N; i++) {
		cin >> name;
		name_num[name] = i;
		num_name[i] = name;
	}

	cin >> M;
	string parent, child;
	for (int i = 0; i < M; i++) {
		cin >> child >> parent;
		int p_index = name_num[parent];
		int c_index = name_num[child];
		v[p_index].push_back(c_index);
		pre[c_index]++;
	}
	
	for (int i = 0; i < N; i++) {
		for (int nxt : v[i]) {
			if (pre[nxt] - pre[i] == 1) {
				v_str[i].push_back(num_name[nxt]);
			}
		}
	}

	for (int i = 0; i < N; i++) {
		sort(v_str[i].begin(), v_str[i].end());
	}
	

	topology();
	sort(roots.begin(), roots.end());

	cout << roots.size()<<"\n";
	for (string root : roots) {
		cout << root << " ";
	}
	cout << "\n";


	string ordered_name;
	while(!ordered_names.empty()){
		ordered_name = ordered_names.top();
		//cout << ordered_name << "\n";
		ordered_names.pop();
		int parent_idx = name_num[ordered_name];
		
		cout << ordered_name << " "<<v_str[parent_idx].size()<<" ";
		for (string child_name : v_str[parent_idx]) {
			cout << child_name << " ";
		}
		cout << "\n";
	}


	return 0;
}