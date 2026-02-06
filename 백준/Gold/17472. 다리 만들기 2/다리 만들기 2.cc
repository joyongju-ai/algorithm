#include <iostream>
#include<cstring>
#include<algorithm>
#include<string>
#include <vector>
#include<queue>

using namespace std;
int n, m;
int MAP[20][20];
int visited[20][20];

int dy[4] = { 0,1,0,-1 };
int dx[4] = { 1,0,-1,0 };
int cnt;
int V;
int total;

int parent[10];

struct Point {
    int y, x;
};

struct Edge {
    int a, b, cost;
};

vector<Edge>edges;
vector<Point> parts[10];

/*부품 구분용 bfs*/
void bfs_sep(Point st) {
    visited[st.y][st.x] = 1;
    queue<Point> q;
    q.push(st);
    parts[cnt + 1].push_back(st);
    MAP[st.y][st.x] = cnt + 1; //이 부분 생각 못함. 부품 번호 붙이기

    while (!q.empty()) {
        Point cp = q.front(); q.pop();

        for (int i = 0; i < 4; i++) {
            Point np = { cp.y + dy[i],cp.x + dx[i] };

            if (np.y < 0 || np.y >= n || np.x < 0 || np.x >= m) {
                continue;
            }
            if (visited[np.y][np.x]) continue;
            if (MAP[np.y][np.x] == 0) continue;

            MAP[np.y][np.x] = cnt + 1;
            visited[np.y][np.x] = 1;
            q.push(np);
            parts[cnt + 1].push_back(np);
        }
    }

}


/*부품 구분*/
/*부품 번호별로 좌표 배열에 넣기*/
int seperate_part() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (MAP[i][j] == 1 && visited[i][j] == 0) {
                bfs_sep({ i,j });
                cnt++;
            }
        }
    }
    return cnt;
}

// 부품 방향별로 bfs
// 직선으로만 움직일 수 있으므로 방향을 고정
// 1베이스 간선
// 처음에 거리가 1인 곳이 2로 나오길래 봤더니 부품을 만나도 계속 진행하고 있었음.
//그래서 다른 부품 만나면 q에 넣지말고 visited도 갱신하지 않게 continue 했더니
// visited[np.y][np.x]가 0인 바람에 cost가 -1이 돼서 안됐다.
// 다른 부품 만났을 때 visted 갱신은 먼저 해주고 q에만 안 넣는 걸로 고쳐서 해결
void bfs_edge(int dir, int v_num) {
    queue<Point> q;
    for (int i = 0; i < parts[v_num].size(); i++) {
        Point st = parts[v_num][i];
        visited[st.y][st.x] = 1;
        q.push(st);
    }


    while (!q.empty()) {
        Point cp = q.front();
        q.pop();
        Point np = { cp.y + dy[dir],cp.x + dx[dir] };

        if (np.y < 0 || np.y >= n || np.x < 0 || np.x >= m) {
            continue;
        }
        if (visited[np.y][np.x]) continue;
        if (MAP[np.y][np.x] == v_num) continue;

        visited[np.y][np.x] = visited[cp.y][cp.x] + 1;
        if (MAP[np.y][np.x] != 0) {
            int cost = visited[np.y][np.x] - 2;
            if (cost > 1) {
                Edge edge = { v_num , MAP[np.y][np.x] ,cost };
                edges.push_back(edge);
            }
            continue;
        }
        q.push(np);
    }
}

void make_edge() {
    int dir;
    for (int i = 1; i < V + 1; i++) {
        for (int j = 0; j < 4; j++) {
            dir = j;
            bfs_edge(dir, i);
            memset(visited, 0, sizeof(visited));
        }
    }
}

bool compare(Edge a, Edge b) {
    return a.cost < b.cost;
}

int find(int x) {
    if (x == parent[x]) {
        return x;
    }
    return parent[x] = find(parent[x]);
}

void setUnion(int a, int b) {
    int t1 = find(a);
    int t2 = find(b);
    if (t1 == t2) {
        return;
    }
    parent[t2] = t1;
}

int kruskal() {
    int selCount = 0;
    int distance = 0;
    for (int i = 0; i < edges.size(); i++) {
        if (find(edges[i].a) == find(edges[i].b)) {
            continue;
        }
        selCount++;
        distance += edges[i].cost;
        setUnion(edges[i].a, edges[i].b);
        //cout << edges[i].a << " " << edges[i].b << " " << edges[i].cost << "\n";
        if (selCount == V - 1) {
            break;
        }
    }
    if (selCount < V - 1) {
        return -1;
    }
    return distance;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> MAP[i][j];
        }
    }
    V = seperate_part();
    memset(visited, 0, sizeof(visited));
    make_edge();

    for (int i = 1; i <= V; i++) {
        parent[i] = i;
    }


    sort(edges.begin(), edges.end(), compare);
    total = kruskal();
    if (total == -1) {
        cout << -1;
    }
    else {
        cout << total;
    }
    return 0;
}


//지도 찍는데 필요한 도구
/*for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << MAP[i][j];
        }
        cout << "\n";
    }*/

    //간선 찍는데 필요한 도구
    /*
    for (Edge c : edges) {
            cout << c.a << " " << c.b << " "<< c.cost<< "\n";
        }
    */