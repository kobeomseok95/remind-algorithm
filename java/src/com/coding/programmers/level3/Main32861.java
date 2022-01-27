package com.coding.programmers.level3;

import java.util.Arrays;

class Main32861 {

    static class Parents {
        int[] parents;

        public Parents(int n) {
            parents = new int[n + 1];
            for (int i = 0; i < n + 1; i++) {
                parents[i] = i;
            }
        }

        public int findParent(int point) {
            if (parents[point] == point) {
                return parents[point];
            }
            return parents[point] = findParent(parents[point]);
        }

        public void union(int a, int b) {
            a = findParent(a);
            b = findParent(b);
            if (a > b) {
                parents[a] = b;
            } else {
                parents[b] = a;
            }
        }
    }

    public int solution(int n, int[][] costs) {
        Arrays.sort(costs, (o1, o2) -> o1[2] - o2[2]);
        Parents parents = new Parents(n);
        int answer = 0;
        for (int[] cost : costs) {
            if (parents.findParent(cost[0]) != parents.findParent(cost[1])) {
                parents.union(cost[0], cost[1]);
                answer += cost[2];
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        Main32861 main = new Main32861();
        System.out.println(main.solution(4,
                new int[][] {
                        {0, 1, 1},
                        {0, 2, 2},
                        {1, 2, 5},
                        {1, 3, 1},
                        {2, 3, 8},
                        {0, 1, 2},
                        {0, 2, 1},
                        {3, 0, 1},
                        {3, 2, 1}
        }));
    }
}
