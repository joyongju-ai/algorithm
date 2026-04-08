#include <iostream>
#include <cmath>
#include<algorithm>
#include<string.h>
#include <vector>
#include<climits>

using namespace std;

int N, M;
int mems[105];
int costs[105];

int dp[105][10005];

int main() {
    cin >> N >> M;

    for (int i = 1; i <= N; i++) {
        cin >> mems[i];
    }

    for (int i = 1; i <= N; i++) {
        cin >> costs[i];
    }

    for (int i = 1; i <= N; i++) {
        for (int j = 0; j <= 10000; j++) {
            dp[i][j] = dp[i - 1][j];
            if (j - costs[i] >= 0) {
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - costs[i]] + mems[i]);
            }
        }
    }

    for (int i = 0; i <= 10000; i++) {
        if (dp[N][i] >= M) {
            cout << i << "\n";
            break;
        }
    }

    return 0;
}