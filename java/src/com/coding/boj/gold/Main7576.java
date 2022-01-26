package com.coding.boj.gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main7576 {

    private static final BufferedReader READER = new BufferedReader(new InputStreamReader(System.in));
    private static final int[][] DIR = {{-1, 1, 0, 0}, {0, 0, -1, 1}};

    private static Queue<TomatoPosition> q = new LinkedList<>();
    private static StringTokenizer st;
    private static int m, n;
    private static int[][] box;
    private static int enableRipeTomatoCount;

    public static void main(String[] args) throws IOException {
        System.out.println(solve());
    }

    private static int solve() throws IOException {
        init();
        return bfs();
    }

    private static void init() throws IOException {
        boxSizeInit();
        enableRipeTomatoCountInit();
        boxArrayAndQueueInit();
    }

    private static void boxSizeInit() throws IOException {
        st = new StringTokenizer(READER.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        box = new int[n][m];
        enableRipeTomatoCount = n * m;
    }

    private static void enableRipeTomatoCountInit() {
        enableRipeTomatoCount = n * m;
    }

    private static void boxArrayAndQueueInit() throws IOException {
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(READER.readLine());
            for (int j = 0; j < m; j++) {
                box[i][j] = Integer.parseInt(st.nextToken());
                addQueueOrMinusEnableRipeTomatoCount(i, j);
            }
        }
    }

    private static void addQueueOrMinusEnableRipeTomatoCount(int i, int j) {
        if (box[i][j] != 0) {
            --enableRipeTomatoCount;
            if (box[i][j] == 1) {
                q.offer(new TomatoPosition(i, j));
            }
        }
    }

    private static int bfs() {
        int days = 0;
        while (!q.isEmpty() && enableRipeTomatoCount != 0) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TomatoPosition position = q.remove();
                for (int d = 0; d < 4; d++) {
                    int ny = position.y + DIR[0][d];
                    int nx = position.x + DIR[1][d];
                    if (0 <= ny && ny < n && 0 <= nx && nx < m && box[ny][nx] == 0) {
                        box[ny][nx] = 1;
                        q.offer(new TomatoPosition(ny, nx));
                        --enableRipeTomatoCount;
                    }
                }
            }
            ++days;
        }
        return enableRipeTomatoCount == 0 ? days : -1 ;
    }

    static class TomatoPosition {
        private int y;
        private int x;

        public TomatoPosition(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }
}
