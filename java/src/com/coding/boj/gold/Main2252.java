package com.coding.boj.gold;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main2252 {

    private static final BufferedReader READER = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer tokenizer;

    public static void main(String[] args) throws IOException {
        tokenizer = new StringTokenizer(READER.readLine());
        int N = Integer.parseInt(tokenizer.nextToken());
        int M = Integer.parseInt(tokenizer.nextToken());
        int[] indegree = new int[N + 1];
        List<Integer>[] graph = initGraph(N);
        for (int i = 0; i < M; i++) {
            tokenizer = new StringTokenizer(READER.readLine());
            int A = Integer.parseInt(tokenizer.nextToken());
            int B = Integer.parseInt(tokenizer.nextToken());
            graph[A].add(B);
            indegree[B]++;
        }
        topologySort(indegree, graph);
    }

    private static List<Integer>[] initGraph(int N) {
        List<Integer>[] graph = new ArrayList[N + 1];
        for (int i = 1; i < N + 1; i++) {
            graph[i] = new ArrayList<>();
        }
        return graph;
    }

    private static void topologySort(int[] indegree, List<Integer>[] graph) {
        Queue<Integer> q = new LinkedList<>();
        for (int i = 1; i < indegree.length; i++) {
            if (indegree[i] == 0) {
                q.offer(i);
            }
        }
        while (!q.isEmpty()) {
            int current = q.poll();
            System.out.print(current + " ");
            for (int next : graph[current]) {
                indegree[next]--;
                if (indegree[next] == 0) {
                    q.add(next);
                }
            }
        }
    }
}
