//swea 4014
//활주로 건설

#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>
#include<vector>

using namespace std;

int arr[20][20];
int N = 0;
int X = 0;

bool one_row_search(int i, int pass_height, int prev, int index) {
	for (int j = 0; j < N; j++) {
		if (arr[i][j] < prev) {
			if ((prev - arr[i][j]) == 1) {
				pass_height = arr[i][j];
				for (int k = j; k < j + X; k++) {
					if (k >= N) {
						return false;
					}
					if (arr[i][k] != pass_height) {
						return false;
					}
				}
				index = j + X;
				j = j + X - 1;
			}
			else {
				return false;
			}
		}
	
		else if (arr[i][j] > prev) {
			if ((arr[i][j] - prev) == 1){
				pass_height = prev;
				for (int k = j - 1; k >= j - X; k--) {
					if (k < index) {
						return false;
					}
					if (arr[i][k] != pass_height) {
						return false;
					}
				}
				index = j;
			}
			else {
				return false;
			}
			
		}
		prev = arr[i][j];
	}
	return true;
}

int row_search() {
	int count = 0;
	for (int i = 0; i < N; i++) {
		int prev = arr[i][0];
		int index = 0;
		int pass_height = 0;
		if (one_row_search(i, pass_height, prev, index)) {
			count++;
		}
	}
	return count;
}

void rotate() {
	int temp_arr[20][20] = { 0 };
	
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			temp_arr[i][j] = arr[i][j];
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			arr[i][j] = temp_arr[N-1-j][i];
		}
	}

	/*
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cout << arr[i][j]<< " ";
		}
		cout << endl;
	}
	*/
	
}

int main() {
	memset(arr, 0,sizeof(arr));
	ios::sync_with_stdio(0);
	cin.tie(0);

	int T;
	int count = 0;
	cin >> T;
	for (int test_case = 1; test_case <= T; test_case++) {
		cin >> N >> X;
		count = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				cin >> arr[i][j];
			}
		}
		count += row_search();
		rotate();
		count += row_search();
		cout << "#" << test_case << " " << count << endl;
	}
	return 0;
}

