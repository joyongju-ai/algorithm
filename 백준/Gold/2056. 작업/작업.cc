// 작업
//백준 2056

#include<iostream>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<vector>
#include<queue>
#include<deque>

using namespace std;



int N;
int indegrees[10005];
vector<int> v[10005];

struct work {
    int node, end;
};

work arr[10005];

int min_time = 0;
int work_times[10005];



void topology() {
    queue<work> q;
    for (int i = 1; i <= N; i++) {
        if (indegrees[i] == 0) {
            q.push({i,work_times[i]});
            arr[i] = { i,work_times[i] };
        }
    }

    while (!q.empty()) {
        work now = q.front();
        q.pop();

        //cout << now.end<<" ";
        if (now.end > min_time) {
            min_time = now.end;
        }

        for (int nxt : v[now.node]) {
            indegrees[nxt]--;
            arr[nxt].end = max(arr[nxt].end, now.end + work_times[nxt]);
            if (indegrees[nxt] == 0) {
                arr[nxt].node = nxt;
                q.push(arr[nxt]);
            }
        }
    }

}



int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N;
    int work_time, num, pre;
    for (int i = 1; i <= N; i++) {
        cin >> work_time;
        work_times[i] = work_time;
        cin >> num;
        if (num > 0) {
            for (int j = 0; j < num; j++) {
                cin >> pre;
                v[pre].push_back(i);
                indegrees[i]++;
            }
        }
    }

    topology();

    cout << min_time << "\n";

    return 0;
}