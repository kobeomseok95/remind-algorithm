package com.coding.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main7576 {

    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final int[][] DIR = {{-1, 1, 0, 0}, {0, 0, -1, 1}};
    private static final Queue<Tomato> Q = new LinkedList<Tomato>();

    private static int M;
    private static int N;
    private static int[][] BOX;
    private static int TOMATOES_COUNT;

    public static void main(String[] args) throws IOException {
        System.out.println(solve());
    }

    private static int solve() throws IOException {
        init();
        return bfs();
    }

    public static void init() throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        BOX = new int[N][M];
        TOMATOES_COUNT = M * N;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                BOX[i][j] = Integer.parseInt(st.nextToken());
                switch (BOX[i][j]) {
                    case 1:
                        Q.offer(new Tomato(i, j));
                    case -1:
                        --TOMATOES_COUNT;
                    default:
                        break;
                }
            }
        }
    }

    private static int bfs() {
        int days = 0;
        while (!Q.isEmpty() && TOMATOES_COUNT != 0) {
            int size = Q.size();
            for (int i = 0; i < size; i++) {
                Tomato tomato = Q.remove();
                for (int d = 0; d < 4; d++) {
                    int ny = tomato.y + DIR[0][d];
                    int nx = tomato.x + DIR[1][d];
                    if (0 <= ny && ny < N && 0 <= nx && nx < M && BOX[ny][nx] == 0) {
                        BOX[ny][nx] = 1;
                        Q.offer(new Tomato(ny, nx));
                        --TOMATOES_COUNT;
                    }
                }
            }
            ++days;
        }
        return TOMATOES_COUNT == 0
                ? days
                : -1;
    }

    static class Tomato {
        private int y;
        private int x;

        public Tomato(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }
}
