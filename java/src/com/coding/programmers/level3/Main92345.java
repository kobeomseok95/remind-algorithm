package com.coding.programmers.level3;

class Main92345 {

    private static final int[] dy = {1, -1, 0, 0};
    private static final int[] dx = {0, 0, -1, 1};
    private static final int MAX = Integer.MAX_VALUE;

    static class GameResult {
        private boolean win;
        private int count;

        public GameResult(boolean win, int count) {
            this.win = win;
            this.count = count;
        }

        public boolean isWin() {
            return win;
        }

        public int getCount() {
            return count;
        }
    }

    public int solution(int[][] board, int[] aloc, int[] bloc) {
        GameResult result = dfs(board, aloc, bloc, 1, 0);
        return result.getCount();
    }

    private GameResult dfs(int[][] board, int[] aloc, int[] bloc, int turn, int moveCount) {
        int ay = aloc[0];
        int ax = aloc[1];
        int by = bloc[0];
        int bx = bloc[1];

        if ((turn > 0 && board[ay][ax] == 0) || (turn < 0 && board[by][bx] == 0)) {
            return new GameResult(false, moveCount);
        }

        int win = MAX;
        int lose = 0;
        for (int d = 0; d < 4; d++) {
            if (turn > 0) {
                int nay = ay + dy[d];
                int nax = ax + dx[d];
                if (0 > nay || 0 > nax || board.length <= nay || board[0].length <= nax) {
                    continue;
                }
                if (board[nay][nax] == 0) {
                    continue;
                }
                board[ay][ax] = 0;
                GameResult result = dfs(board, new int[] {nay, nax}, bloc, -turn, moveCount + 1);
                if (!result.isWin()) {
                    win = Math.min(win, result.getCount());
                } else {
                    lose = Math.max(lose, result.getCount());
                }
                board[ay][ax] = 1;
            } else {
                int nby = by + dy[d];
                int nbx = bx + dx[d];
                if (0 > nby || 0 > nbx || board.length <= nby || board[0].length <= nbx) {
                    continue;
                }
                if (board[nby][nbx] == 0) {
                    continue;
                }
                board[by][bx] = 0;
                GameResult result = dfs(board, aloc, new int[]{nby, nbx}, -turn, moveCount + 1);
                if (!result.isWin()) {
                    win = Math.min(win, result.getCount());
                } else {
                    lose = Math.max(lose, result.getCount());
                }
                board[by][bx] = 1;
            }
        }

        if (win == MAX && lose == 0) {
            return new GameResult(false, moveCount);
        } else if (win != MAX) {
            return new GameResult(true, win);
        } else {
            return new GameResult(false, lose);
        }
    }
}
