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
}
