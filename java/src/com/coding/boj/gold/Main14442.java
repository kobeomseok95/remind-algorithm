package com.coding.boj.gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Main14442 {

    private static final BufferedReader READER = new BufferedReader(new InputStreamReader(System.in));
    private static final int[] dy = {-1, 1, 0, 0};
    private static final int[] dx = {0, 0, -1, 1};
    private static int n, m, k;
    private static int[][] map;
    private static boolean[][][] visit;

    public static void main(String[] args) throws IOException {
        init();
        bfs();
    }

    private static void init() throws IOException {
        StringTokenizer tokenizer = new StringTokenizer(READER.readLine());
        n = Integer.parseInt(tokenizer.nextToken());
        m = Integer.parseInt(tokenizer.nextToken());
        k = Integer.parseInt(tokenizer.nextToken());
        map = new int[n][m];
        visit = new boolean[n][m][k + 1];
        for (int i = 0; i < n; i++) {
            String[] inputs = READER.readLine().split("");
            for (int j = 0; j < m; j++) {
                map[i][j] = Integer.parseInt(inputs[j]);
            }
        }
    }

    private static void bfs() {
        Queue<Position> q = new LinkedList<>();
        q.offer(new Position(0, 0, 0, k));
        visit[0][0][k] = true;

        while (!q.isEmpty()) {
            Position current = q.poll();
            if (current.y == n - 1 && current.x == m - 1) {
                System.out.println(current.moveCount + 1);
                return;
            }

            for (int d = 0; d < 4; d++) {
                int ny = current.y + dy[d];
                int nx = current.x + dx[d];
                if (isRange(ny, nx)) {
                    if (map[ny][nx] == 0 && !visit[ny][nx][current.remainBreakCount]) {
                        q.offer(new Position(ny, nx, current.moveCount + 1, current.remainBreakCount));
                        visit[ny][nx][current.remainBreakCount] = true;
                    } else if (map[ny][nx] == 1 && current.enableBreakWall() && !visit[ny][nx][current.remainBreakCount - 1]) {
                        q.offer(new Position(ny, nx, current.moveCount + 1, current.remainBreakCount - 1));
                        visit[ny][nx][current.remainBreakCount - 1] = true;
                    }
                }
            }
        }
        System.out.println(-1);
    }

    private static boolean isRange(int ny, int nx) {
        return 0 <= ny && ny < n && 0 <= nx && nx < m;
    }

    static class Position {
        int y;
        int x;
        int moveCount;
        int remainBreakCount;

        public Position(int y, int x, int moveCount, int remainBreakCount) {
            this.y = y;
            this.x = x;
            this.moveCount = moveCount;
            this.remainBreakCount = remainBreakCount;
        }

        public boolean enableBreakWall() {
            return remainBreakCount > 0;
        }
    }
}
