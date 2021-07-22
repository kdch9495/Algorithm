// https://programmers.co.kr/learn/courses/30/lessons/42840

import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] answer = {};
		int[] a = {1,2,3,4,5}; // 5개
		int[] b = {2,1,2,3,2,4,2,5}; // 8개
		int[] c = {3,3,1,1,2,2,4,4,5,5 }; // 10개

		int a_cnt = 0;
		int b_cnt = 0;
		int c_cnt = 0;

		for (int i = 0; i < answer.length; i++) {
			if (a[i % a.length] == answer[i]) {
				a_cnt++;
			}
			if (b[i % b.length] == answer[i]) {
				b_cnt++;
			}
			if (c[i % c.length] == answer[i]) {
				c_cnt++;
			}
		}

		List<Integer> list = new ArrayList<>();

		int max = Math.max(a_cnt, Math.max(b_cnt, c_cnt));

		if(a_cnt == max) {
			list.add(1);
		}
		if(b_cnt == max) {
			list.add(2);
		}
		if(c_cnt == max) {
			list.add(3);
		}
		
		answer = new int[list.size()];
		
		for(int i=0; i<answer.length; i++) {
			answer[i] = list.get(i);
			System.out.println(answer[i]);
		}
		
		
		return answer;
    }
}
