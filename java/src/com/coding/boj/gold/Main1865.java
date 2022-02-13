package com.coding.boj.gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

class Main1865 {

    static class Road {
        int start, end, cost;

        public Road(int start, int end, int cost) {
            this.start = start;
            this.end = end;
            this.cost = cost;
        }
    }

    private static final BufferedReader READER = new BufferedReader(new InputStreamReader(System.in));
    private static final String YES = "YES";
    private static final String NO = "NO";
    private static final int INF = 500 * 10_000;

    private static int N, M, W;
    private static Road[] roads;
    private static int[] dist;
    private static StringTokenizer tokenizer;

    public static void main(String[] args) throws IOException {
        int TC = Integer.parseInt(READER.readLine());
        StringBuilder stringBuilder = new StringBuilder();
        for (int i = 0; i < TC; i++) {
            init();

            if (bellmanFord()) {
                stringBuilder.append(YES);
            } else {
                stringBuilder.append(NO);
            }
            stringBuilder.append("\n");
        }
        System.out.println(stringBuilder);
    }

    private static void init() throws IOException {
        tokenizer = new StringTokenizer(READER.readLine());
        N = Integer.parseInt(tokenizer.nextToken());
        M = Integer.parseInt(tokenizer.nextToken());
        W = Integer.parseInt(tokenizer.nextToken());
        dist = new int[N + 1];
        roads = new Road[2 * M + W];
        int index = 0;
        for (int i = 0; i < M + W; i++) {
            tokenizer = new StringTokenizer(READER.readLine());
            int S = Integer.parseInt(tokenizer.nextToken());
            int E = Integer.parseInt(tokenizer.nextToken());
            int T = Integer.parseInt(tokenizer.nextToken());
            if (i < M) {
                roads[index++] = new Road(S, E, T);
                roads[index++] = new Road(E, S, T);
            } else {
                roads[index++] = new Road(S, E, -T);
            }
        }
    }

    private static boolean bellmanFord() {
        Arrays.fill(dist, INF);
        dist[1] = 0;
        boolean isUpdate = false;

        for (int i = 1; i <= N; i++) {
            isUpdate = false;
            for (int j = 0; j < roads.length; j++) {
                Road road = roads[j];
                if (dist[road.end] > dist[road.start] + road.cost) {
                    dist[road.end] = dist[road.start] + road.cost;
                    isUpdate = true;
                }
            }
            if (!isUpdate) {
                break;
            }
        }
        return isUpdate;
    }
}
