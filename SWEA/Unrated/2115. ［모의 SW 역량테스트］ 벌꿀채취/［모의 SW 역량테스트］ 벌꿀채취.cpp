//swea 2115
//벌꿀채취


#include <iostream>
#include <cstring>
#include<string>
#include<algorithm>

using namespace std;
int n, m, c;
int MAP[11][11];
int power[10];
int max_profits[2];
int max_profit_sum;

//개수 상과없이 뽑아서 비교하는 조합 재귀
void dfs(int row, int col, int next, int lev,int profit,int total,int max_profit_num) {
	max_profits[max_profit_num] = max(profit, max_profits[max_profit_num]);
	if (lev == m) {
		return;
	}

	for (int i = next; i < m; i++) {
		int add_num = MAP[row][col + i];
		if (total + add_num > c) continue;
		dfs(row, col, i + 1, lev + 1, profit + power[add_num],total + add_num,max_profit_num);
	}

}


int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int T;
	cin >> T;
	for (int i = 1; i < 10; i++) {
		power[i] = i * i;
	}

	for (int test_case = 1; test_case <= T; test_case++) {
		memset(MAP, 0, sizeof(MAP));
		memset(max_profits, 0, sizeof(max_profits));
		cin >> n >> m >> c;
		max_profit_sum = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cin >> MAP[i][j];
			}
		}
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n - m + 1; j++) {
				for (int k = 0; k < n; k++) {
					for (int l = 0; l < n - m + 1; l++) {
						if ((j + m - 1) >= l && (i == k)) continue;
						dfs(i, j, 0, 0, 0, 0, 0);
						dfs(k, l, 0, 0, 0, 0, 1);
						max_profit_sum = max(max_profit_sum,max_profits[0] + max_profits[1]);
						memset(max_profits, 0, sizeof(max_profits));
					}
				}
			}
		}
		cout << "#" << test_case << " " << max_profit_sum <<"\n";
	}

	return 0;
}