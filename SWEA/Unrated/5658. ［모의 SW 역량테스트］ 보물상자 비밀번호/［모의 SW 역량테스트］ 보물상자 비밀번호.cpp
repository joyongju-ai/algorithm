#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<deque>
 
using namespace std;
 
void rotate(deque<char>& dq) {
    char ch = dq.back();
    dq.pop_back();
    dq.push_front(ch);
}
 
bool isExist(int side_num, const vector<int>& nums) {
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] == side_num) return true;
    }
    return false;
}
 
int main() {
    int T;
    cin >> T;
    for (int test_case = 1; test_case <= T; test_case++) {
        int N, K, size;
        string side_num;
        cin >> N >> K;
        size = N / 4;
        vector<int> nums;
        deque<char> dq;
        string input;
        cin >> input;
 
        for (char c : input) {
            dq.push_back(c);
        }
 
        int t = 0;
        for (int k = 0; k < N; k++) {
            t = 0;
            for (int i = 0; i < 4; i++) {
                side_num = "";
                for (int j = 0; j < size; j++) {
                    side_num += dq[t++];
                }
                int val = stoi(side_num, nullptr, 16);
                if (!isExist(val, nums)) {
                    nums.push_back(val);
                }
            }
            rotate(dq);
        }
        sort(nums.begin(), nums.end(), greater<int>());
        cout << "#" <<test_case<<" "<<  int(nums[K - 1]) << endl;
    }
 
}