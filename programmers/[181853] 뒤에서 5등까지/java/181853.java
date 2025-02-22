import java.util.*;

class Solution {
    public int[] solution(int[] num_list) {
        return Arrays.stream(num_list)
            .sorted() // 오름차순 정렬
            .limit(5) // 가장 작은 5개 요소
            .toArray(); // int로 변환
    }
}