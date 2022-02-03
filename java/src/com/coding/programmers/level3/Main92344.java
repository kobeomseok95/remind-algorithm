package com.coding.programmers.level3;

class Main92344 {

    public int solution(int[][] board, int[][] skill) {
        int[][] prefixArr = makePrefixArr(board, skill);
        return countUndestroyedBuilding(board, prefixArr);
    }

    private int[][] makePrefixArr(int[][] board, int[][] skill) {
        int[][] prefixArr = new int[board.length + 1][board[0].length + 1];
        for (int[] row : skill) {
            int type = row[0];
            int r1 = row[1];
            int c1 = row[2];
            int r2 = row[3];
            int c2 = row[4];
            int degree = type == 1 ? -row[5] : row[5];

            for (int i = r1; i <= r2; i++) {
                prefixArr[i][c1] += degree;
                prefixArr[i][c2 + 1] += -degree;
            }
        }
        return prefixArr;
    }

    private int countUndestroyedBuilding(int[][] board, int[][] prefixArr) {
        int answer = 0;
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (j != 0)
                    prefixArr[i][j] += prefixArr[i][j - 1];

                board[i][j] += prefixArr[i][j];
                if (board[i][j] > 0)
                    answer++;
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        Main92344 main = new Main92344();
        System.out.println(main.solution(new int[][] {
                {5,5,5,5,5},
                {5,5,5,5,5},
                {5,5,5,5,5},
                {5,5,5,5,5}
        }, new int[][] {
                {1,0,0,3,4,4},
                {1,2,0,2,3,2},
                {2,1,0,3,1,2},
                {1,0,1,3,3,1}
        }));
        System.out.println(main.solution(new int[][] {
                {1,2,3},
                {4,5,6},
                {7,8,9}
        }, new int[][] {
                {1,1,1,2,2,4},
                {1,0,0,1,1,2},
                {2,2,0,2,0,100}
        }));
    }
}
