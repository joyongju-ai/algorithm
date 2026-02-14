// 백준 17406 배열 돌리기 4 (A형 기출 스타일 구현)

#include<iostream>
#include<cstring> // memset, memcpy 사용을 위한 헤더
#include<vector>
#include<queue>
#include<algorithm> // min 사용
#include<deque>     // 회전 로직의 핵심
#include<climits>   // INT_MAX 사용 (21e8 대신 안전하게)

using namespace std;

// 전역 변수 선언 (메모리 스택 오버플로우 방지 및 편의성)
int arr[55][55];      // 입력받는 원본 배열 (절대 변하지 않음)
int copy_arr[55][55]; // 시뮬레이션용 배열 (회전시키고 계산하는 용도)
int N, M, K;
int min_arr_val;      // 최종 정답을 저장할 변수

// 회전 연산 정보를 담을 구조체
struct Rotate_op {
    int r, c, s;
};
Rotate_op rotate_op[10]; // 최대 6개의 연산

// 순열(Permutation) 생성을 위한 배열들
int visited[10]; // 방문 체크
int path[10];    // 정해진 순서를 저장할 배열

/**
 * @brief 특정 껍질(Shell)들을 Deque를 이용해 회전시키는 함수
 * @param index 수행할 회전 연산의 번호
 */
void rotate(int index) {
    deque<int> dq;
    
    // 구조체에서 r, c, s 가져오기
    int s = rotate_op[index].s;
    int r = rotate_op[index].r;
    int c = rotate_op[index].c;

    // 회전시킬 사각형의 가장 바깥쪽 좌표 설정
    // (y1, x1) = 좌상단, (y2, x2) = 우하단
    int y1 = r - s;
    int x1 = c - s;
    int y2 = r + s;
    int x2 = c + s;

    // 껍질의 개수(s)만큼 안쪽으로 파고들며 반복
    // 예: s=2면 바깥쪽 테두리 -> 안쪽 테두리 순서로 수행
    for (int k = 0; k < s; k++) {
        dq.clear(); // 덱 초기화

        // -------------------------------------------------
        // 1단계: 껍질의 값들을 1줄로 펴서 Deque에 담기 (Extract)
        // -------------------------------------------------
        
        // 위쪽 벽 (왼 -> 오)
        for (int i = x1; i < x2; i++) dq.push_back(copy_arr[y1][i]);
        // 오른쪽 벽 (위 -> 아래)
        for (int i = y1; i < y2; i++) dq.push_back(copy_arr[i][x2]);
        // 아래쪽 벽 (오 -> 왼)
        for (int i = x2; i > x1; i--) dq.push_back(copy_arr[y2][i]);
        // 왼쪽 벽 (아래 -> 위)
        for (int i = y2; i > y1; i--) dq.push_back(copy_arr[i][x1]);

        // -------------------------------------------------
        // 2단계: 회전 (Rotate) - 시계 방향 1칸
        // -------------------------------------------------
        // 뒤에 있는 놈을 빼서 앞으로 보냄 (오른쪽으로 한 칸 미는 효과)
        dq.push_front(dq.back());
        dq.pop_back();

        // -------------------------------------------------
        // 3단계: 회전된 값을 다시 배열에 덮어쓰기 (Insert)
        // -------------------------------------------------
        // 1단계에서 뽑았던 순서 그대로 다시 넣음
        
        // 위쪽 벽
        for (int i = x1; i < x2; i++) {
            copy_arr[y1][i] = dq.front();
            dq.pop_front();
        }
        // 오른쪽 벽
        for (int i = y1; i < y2; i++) {
            copy_arr[i][x2] = dq.front();
            dq.pop_front();
        }
        // 아래쪽 벽
        for (int i = x2; i > x1; i--) {
            copy_arr[y2][i] = dq.front();
            dq.pop_front();
        }
        // 왼쪽 벽
        for (int i = y2; i > y1; i--) {
            copy_arr[i][x1] = dq.front();
            dq.pop_front();
        }

        // -------------------------------------------------
        // 4단계: 다음 안쪽 껍질로 좌표 좁히기
        // -------------------------------------------------
        x1 += 1; y1 += 1; // 좌상단은 우하향
        x2 -= 1; y2 -= 1; // 우하단은 좌상향
    }
}

/**
 * @brief 현재 copy_arr 상태에서 각 행의 합 중 최솟값을 구하는 함수
 */
int arr_cal() {
    int local_min = INT_MAX; // 지역 최솟값 초기화
    for (int i = 0; i < N; i++) {
        int row_sum = 0;
        for (int j = 0; j < M; j++) {
            row_sum += copy_arr[i][j];
        }
        local_min = min(local_min, row_sum);
    }
    return local_min;
}

/**
 * @brief DFS를 이용한 순열 생성 및 시뮬레이션 실행
 * @param lev 현재 선택된 연산의 개수 (Depth)
 */
void dfs(int lev) {
    // [기저 조건] K개의 연산 순서가 모두 정해졌을 때
    if (lev == K) {
        // 1. 원본(arr)을 사본(copy_arr)으로 복사 (초기화)
        // memcpy(목적지, 원본, 바이트크기)
        memcpy(copy_arr, arr, sizeof(arr));

        // 2. 정해진 순서(path)대로 회전 수행
        for (int i = 0; i < K; i++) {
            rotate(path[i]);
        }
        
        // 3. 배열 값 계산 후 전체 최솟값 갱신
        int current_val = arr_cal();
        min_arr_val = min(current_val, min_arr_val);
        
        return;
    }

    // [재귀] 순열 만들기
    for (int i = 0; i < K; i++) {
        if (visited[i]) continue; // 이미 선택한 연산은 패스

        path[lev] = i;      // 순서 기록
        visited[i] = 1;     // 사용 체크
        
        dfs(lev + 1);       // 다음 단계로
        
        visited[i] = 0;     // 원상 복구 (백트래킹)
        path[lev] = -1; // (필수는 아님, 덮어써지므로)
    }
}

int main() {
    // 입출력 속도 향상
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);


    min_arr_val = INT_MAX; // 21e8보다 안전한 정수 최댓값
    // ---------------------

    cin >> N >> M >> K;

    // 배열 입력
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> arr[i][j];
            // 여기서 copy_arr에 넣을 필요 없음 (DFS 안에서 memcpy 함)
        }
    }

    // 회전 연산 입력
    int r, c, s;
    for (int i = 0; i < K; i++) {
        cin >> r >> c >> s;
        // 문제 좌표는 (1,1) 시작이므로 (0,0) 기반으로 변환하여 저장
        rotate_op[i] = { r - 1, c - 1, s };
    }

    // 순열 생성 및 시뮬레이션 시작
    dfs(0);

    // 결과 출력 (삼성 SW 역량테스트 포맷)
    cout << min_arr_val << "\n";

    return 0;
}
