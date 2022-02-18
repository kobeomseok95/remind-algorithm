package com.coding.boj.gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Main1726 {

    static class Position {
        private int y;
        private int x;
        private int dir;
        private int count;

        public Position(int y, int x, int dir) {
            this.y = y;
            this.x = x;
            this.dir = dir;
            this.count = 0;
        }

        public Position(int y, int x, int dir, int count) {
            this.y = y;
            this.x = x;
            this.dir = dir;
            this.count = count;
        }
    }

    private static final BufferedReader READER = new BufferedReader(new InputStreamReader(System.in));
    private final static int[] dy = {-1, 0, 1, 0};
    private final static int[] dx = {0, 1, 0, -1};

    private static int[][] map;
    private static Position start;
    private static Position end;
    private static boolean[][][] visit;
    private static int M;
    private static int N;

    public static void main(String[] args) throws IOException {
        init();
        bfs();
    }

    private static void init() throws IOException {
        StringTokenizer tokenizer = new StringTokenizer(READER.readLine());
        M = Integer.parseInt(tokenizer.nextToken());
        N = Integer.parseInt(tokenizer.nextToken());
        map = new int[M][N];
        for (int i = 0; i < M; i++) {
            tokenizer = new StringTokenizer(READER.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(tokenizer.nextToken());
            }
        }
        tokenizer = new StringTokenizer(READER.readLine());
        start = new Position(Integer.parseInt(tokenizer.nextToken()) - 1, Integer.parseInt(tokenizer.nextToken()) - 1,
                convertDir(Integer.parseInt(tokenizer.nextToken())));
        tokenizer = new StringTokenizer(READER.readLine());
        end = new Position(Integer.parseInt(tokenizer.nextToken()) - 1, Integer.parseInt(tokenizer.nextToken()) - 1,
                convertDir(Integer.parseInt(tokenizer.nextToken())));
    }

    private static int convertDir(int dir) {
        switch (dir) {
            case 2:
                return 3;
            case 3:
                return 2;
            case 4:
                return 0;
            default:
                return 1;
        }
    }

    private static void bfs() {
        Queue<Position> q = new LinkedList<>();
        visit = new boolean[M][N][4];
        q.offer(start);
        visit[start.y][start.x][start.dir] = true;

        while (!q.isEmpty()) {
            Position pos = q.poll();
            if (isEnd(pos)) {
                System.out.println(pos.count);
                return;
            }
            for (int d = 1; d <= 3; d++) {
                int ny = pos.y + (dy[pos.dir] * d);
                int nx = pos.x + (dx[pos.dir] * d);
                if (enableNextStep(ny, nx)) {
                    if (!visit[ny][nx][pos.dir]) {
                        q.offer(new Position(ny, nx, pos.dir, pos.count + 1));
                        visit[ny][nx][pos.dir] = true;
                    }
                } else {
                    break;
                }
            }
            // 방향 전환
            for (int d = 0; d < 4; d++) {
                if (pos.dir != d && !visit[pos.y][pos.x][d]) {
                    int turn = 1;
                    if (pos.dir == 0) {
                        if (d == 2) {
                            turn++;
                        }
                    } else if (pos.dir == 1) {
                        if (d == 3) {
                            turn++;
                        }
                    } else if (pos.dir == 2) {
                        if (d == 0) {
                            turn++;
                        }
                    } else {
                        if (d == 1) {
                            turn++;
                        }
                    }
                    visit[pos.y][pos.x][d] = true;
                    q.offer(new Position(pos.y, pos.x, d, pos.count + turn));
                }
            }
        }
    }

    private static boolean isEnd(Position pos) {
        return end.y == pos.y
                && end.x == pos.x
                && end.dir == pos.dir;
    }

    private static boolean enableNextStep(int y, int x) {
        return 0 <= y
                && y < M
                && 0 <= x
                && x < N
                && map[y][x] == 0;
    }
}
