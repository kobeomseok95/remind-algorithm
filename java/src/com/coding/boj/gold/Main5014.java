package com.coding.boj.gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Main5014 {

    private static final String USE_THE_STAIRS = "use the stairs";
    private static final BufferedReader READER = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer tokenizer;

    public static void main(String[] args) throws IOException {
        tokenizer = new StringTokenizer(READER.readLine());
        int F = Integer.parseInt(tokenizer.nextToken());
        int S = Integer.parseInt(tokenizer.nextToken());
        int G = Integer.parseInt(tokenizer.nextToken());
        int U = Integer.parseInt(tokenizer.nextToken());
        int D = Integer.parseInt(tokenizer.nextToken());
        D = -D;
        System.out.println(bfs(F, S, G, U, D, new int[F + 1]));
    }

    private static String bfs(int F, int S, int G, int U, int D, int[] visit) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(S);
        visit[S] = 1;

        while (!q.isEmpty()) {
            int current = q.poll();
            if (current == G) {
                return String.valueOf(visit[current] - 1);
            }
            int up = current + U;
            if (1 <= up && up <= F && visit[up] == 0) {
                visit[up] = visit[current] + 1;
                q.offer(up);
            }
            int down = current + D;
            if (1 <= down && down <= F && visit[down] == 0) {
                visit[down] = visit[current] + 1;
                q.offer(down);
            }
        }
        return USE_THE_STAIRS;
    }
}
