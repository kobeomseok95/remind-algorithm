package com.coding.boj.gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main1005 {

    private static final BufferedReader READER = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer tokenizer;

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(READER.readLine());
        for (int i = 0; i < T; i++) {
            System.out.println(solve());
        }
    }

    private static int solve() throws IOException {
        tokenizer = new StringTokenizer(READER.readLine());
        int N = Integer.parseInt(tokenizer.nextToken());
        int K = Integer.parseInt(tokenizer.nextToken());
        int[] timePerBuilding = createTimePerBuilding(N);
        List<Integer>[] edges = initEdges(N);
        int[] indegree = createIndegreeAndSetUpEdges(N, K, edges);
        return topologySort(N, indegree, timePerBuilding, edges);
    }

    private static int[] createTimePerBuilding(int N) throws IOException {
        int[] timePerBuilding = new int[N + 1];
        tokenizer = new StringTokenizer(READER.readLine());
        for (int i = 1; i <= N; i++) {
            timePerBuilding[i] = Integer.parseInt(tokenizer.nextToken());
        }
        return timePerBuilding;
    }

    private static List<Integer>[] initEdges(int N) throws IOException {
        List<Integer>[] edges = new ArrayList[N + 1];
        for (int i = 1; i <= N; i++) {
            edges[i] = new ArrayList<>();
        }
        return edges;
    }

    private static int[] createIndegreeAndSetUpEdges(int N, int K, List<Integer>[] edges) throws IOException {
        int[] indegree = new int[N + 1];
        for (int i = 0; i < K; i++) {
            tokenizer = new StringTokenizer(READER.readLine());
            int S = Integer.parseInt(tokenizer.nextToken());
            int E = Integer.parseInt(tokenizer.nextToken());
            edges[S].add(E);
            indegree[E]++;
        }
        return indegree;
    }

    private static int topologySort(int N, int[] indegree, int[] timePerBuilding, List<Integer>[] edges) throws IOException {
        int W = Integer.parseInt(READER.readLine());
        int[] buildTime = new int[N + 1];
        Queue<Integer> q = setUpQAndBuildTime(N, indegree, timePerBuilding, buildTime);

        while (!q.isEmpty()) {
            int current = q.poll();
            for (int next : edges[current]) {
                buildTime[next] = Math.max(buildTime[next], timePerBuilding[next] + buildTime[current]);
                --indegree[next];
                if (indegree[next] == 0) {
                    q.offer(next);
                }
            }
        }

        return buildTime[W];
    }

    private static Queue<Integer> setUpQAndBuildTime(int N, int[] indegree, int[] timePerBuilding, int[] buildTime) {
        Queue<Integer> q = new LinkedList<>();
        for (int i = 1; i <= N; i++) {
            if (indegree[i] == 0) {
                buildTime[i] = timePerBuilding[i];
                q.offer(i);
            }
        }
        return q;
    }
}
