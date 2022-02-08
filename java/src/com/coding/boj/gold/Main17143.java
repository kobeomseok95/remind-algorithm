package com.coding.boj.gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Main17143 {

    private static final BufferedReader READER = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer tokenizer;
    private static final int[] dy = {-1, 0, 1, 0};
    private static final int[] dx = {0, -1, 0, 1};

    static class Shark {
        int row;
        int col;
        int speed;
        int direction;
        int size;

        public Shark(int r, int c, int s, int d, int z) {
            this.row = r;
            this.col = c;
            this.speed = s;
            this.direction = d;
            this.size = z;
        }

        public boolean isNorthOrSouthDirection() {
            return direction == 0 || direction == 2;
        }

        public void changeSpeed(int s) {
            speed %= s;
        }

        public void setRow(int row) {
            this.row = row;
        }

        public void setCol(int col) {
            this.col = col;
        }

        public void changeDirection(int dy, int dx) {
            row -= dy;
            col -= dx;
            direction = (direction + 2) % 4;
        }
    }

    public static void main(String[] args) throws IOException {
        tokenizer = new StringTokenizer(READER.readLine(), " ");
        int R = Integer.parseInt(tokenizer.nextToken());
        int C = Integer.parseInt(tokenizer.nextToken());
        int M = Integer.parseInt(tokenizer.nextToken());
        Shark[][] map = new Shark[R][C];
        for (int i = 0; i < M; i++) {
            tokenizer = new StringTokenizer(READER.readLine(), " ");
            int r = Integer.parseInt(tokenizer.nextToken());
            int c = Integer.parseInt(tokenizer.nextToken());
            int s = Integer.parseInt(tokenizer.nextToken());
            int d = Integer.parseInt(tokenizer.nextToken());
            int z = Integer.parseInt(tokenizer.nextToken());
            map[r - 1][c - 1] = new Shark(r - 1, c - 1, s, changeDirectionForSolving(d), z);
        }

        int answer = 0;
        for (int col = 0; col < C; col++) {
            for (int row = 0; row < R; row++) {
                if (map[row][col] != null) {
                    answer += map[row][col].size;
                    map[row][col] = null;
                    break;
                }
            }

            Queue<Shark> q = new LinkedList<>();
            for (int i = 0; i < R; i++) {
                for (int j = 0; j < C; j++) {
                    if (map[i][j] != null) {
                        q.add(new Shark(i, j, map[i][j].speed, map[i][j].direction, map[i][j].size));
                    }
                }
            }
            map = new Shark[R][C];
            while (!q.isEmpty()) {
                Shark shark = q.poll();
                if (shark.isNorthOrSouthDirection())
                    shark.changeSpeed((R - 1) * 2);
                else
                    shark.changeSpeed((C - 1) * 2);
                for (int s = 0; s < shark.speed; s++) {
                    int newR = shark.row + dy[shark.direction];
                    int newC = shark.col + dx[shark.direction];
                    if (0 > newR || R <= newR || 0 > newC || C <= newC) {
                        shark.changeDirection(dy[shark.direction], dx[shark.direction]);
                        continue;
                    }
                    shark.setRow(newR);
                    shark.setCol(newC);
                }

                if (map[shark.row][shark.col] != null) {
                    Shark sourceShark = map[shark.row][shark.col];
                    if (sourceShark.size < shark.size) {
                        map[shark.row][shark.col] = new Shark(shark.row, shark.col, shark.speed, shark.direction, shark.size);
                    }
                } else {
                    map[shark.row][shark.col] = new Shark(shark.row, shark.col, shark.speed, shark.direction, shark.size);
                }
            }
        }
        System.out.println(answer);
    }

    private static int changeDirectionForSolving(int d) {
        if (d == 1) {
            return 0;
        } else if (d == 2) {
            return 2;
        } else if (d == 3) {
            return 3;
        } else {
            return 1;
        }
    }
}
