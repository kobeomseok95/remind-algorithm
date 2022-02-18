package com.coding.boj.gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main11779 {

    static class Node implements Comparable<Node>{
        private int point;
        private int cost;

        public Node(int point, int cost) {
            this.point = point;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node target) {
            return this.cost - target.cost;
        }
    }

    private static final BufferedReader READER = new BufferedReader(new InputStreamReader(System.in));
    private static final int INF = Integer.MAX_VALUE;
    private static int n, m, start, end;
    private static List<Node>[] edges;
    private static int[] dist;
    private static int[] routeArr;
    private static boolean[] visited;

    public static void main(String[] args) throws IOException {
        init();
        dijkstra();
        printAnswer();
    }

    private static void init() throws IOException {
        n = Integer.parseInt(READER.readLine());
        m = Integer.parseInt(READER.readLine());
        edges = new ArrayList[n + 1];
        dist = new int[n + 1];
        Arrays.fill(dist, INF);
        routeArr = new int[n + 1];
        visited = new boolean[n + 1];
        for (int i = 0; i <= n; i++) {
            edges[i] = new ArrayList<>();
        }
        StringTokenizer tokenizer;
        for (int i = 0; i < m; i++) {
            tokenizer = new StringTokenizer(READER.readLine());
            int a = Integer.parseInt(tokenizer.nextToken());
            int b = Integer.parseInt(tokenizer.nextToken());
            int cost = Integer.parseInt(tokenizer.nextToken());
            edges[a].add(new Node(b, cost));
        }
        tokenizer = new StringTokenizer(READER.readLine());
        start = Integer.parseInt(tokenizer.nextToken());
        end = Integer.parseInt(tokenizer.nextToken());
    }

    private static void dijkstra() {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(start, 0));
        dist[start] = 0;
        routeArr[start] = 0;

        while (!pq.isEmpty()) {
            Node current = pq.poll();
            if (!visited[current.point]) {
                visited[current.point] = true;
            } else {
                continue;
            }

            for (Node next : edges[current.point]) {
                if (dist[next.point] > dist[current.point] + next.cost) {
                    dist[next.point] = dist[current.point] + next.cost;
                    pq.offer(new Node(next.point, dist[next.point]));
                    routeArr[next.point] = current.point;
                }
            }
        }
    }

    private static void printAnswer() {
        System.out.println(dist[end]);

        List<Integer> routes = new ArrayList<>();
        int retrieve = end;
        while (retrieve != 0) {
            routes.add(retrieve);
            retrieve = routeArr[retrieve];
        }
        System.out.println(routes.size());
        for (int i = routes.size() - 1; i >= 0; i--) {
            System.out.print(routes.get(i) + " ");
        }
    }
}
