package com.coding.boj.gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main1766 {

    private static final BufferedReader READER = new BufferedReader(new InputStreamReader(System.in));
    private static int N, M;
    private static StringTokenizer tokenizer;
    private static StringBuilder stringBuilder = new StringBuilder();

    public static void main(String[] args) throws IOException {
        tokenizer = new StringTokenizer(READER.readLine());
        N = Integer.parseInt(tokenizer.nextToken());
        M = Integer.parseInt(tokenizer.nextToken());
        List<Integer>[] edges = initEdges();
        int[] indegree = initIndegree(edges);
        topologySort(edges, indegree);

        System.out.println(stringBuilder.toString());
    }

    private static int[] initIndegree(List<Integer>[] edges) throws IOException {
        int[] indegree = new int[N + 1];
        for (int i = 0; i < M; i++) {
            tokenizer = new StringTokenizer(READER.readLine());
            int A = Integer.parseInt(tokenizer.nextToken());
            int B = Integer.parseInt(tokenizer.nextToken());
            edges[A].add(B);
            indegree[B] += 1;
        }
        return indegree;
    }

    private static List<Integer>[] initEdges() {
        List<Integer>[] edges = new ArrayList[N + 1];
        for (int i = 0; i <= N; i++) {
            edges[i] = new ArrayList<>();
        }
        return edges;
    }

    private static void topologySort(List<Integer>[] edges, int[] indegree) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i = 1; i <= N; i++) {
            if (indegree[i] == 0) {
                pq.add(i);
            }
        }
        while (!pq.isEmpty()) {
            int current = pq.poll();
            stringBuilder.append(current).append(" ");
            for (int next : edges[current]) {
                indegree[next] -= 1;
                if (indegree[next] == 0) {
                    pq.add(next);
                }
            }
        }
    }
}
