package com.coding.boj.gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main1525 {

    private static final BufferedReader READER = new BufferedReader(new InputStreamReader(System.in));
    private static final String CORRECT = "123456780";
    private static final int[] dy = {-1, 1, 0, 0};
    private static final int[] dx = {0, 0, -1, 1};

    private static StringTokenizer tokenizer;
    private static Map<String, Integer> map = new HashMap<>();
    private static String init = "";

    public static void main(String[] args) throws IOException {
        init();
        bfs();
    }

    private static void init() throws IOException {
        for (int i = 0; i < 3; i++) {
            tokenizer = new StringTokenizer(READER.readLine());
            for (int j = 0; j < 3; j++) {
                init += tokenizer.nextToken();
            }
        }
        map.put(init, 0);
    }

    private static void bfs() {
        Queue<String> q = new LinkedList<>();
        q.offer(init);
        while (!q.isEmpty()) {
            String current = q.poll();
            if (current.equals(CORRECT)) {
                System.out.println((map.get(current)));
                return;
            }

            int currentZeroIndex = current.indexOf('0');
            int zeroY = currentZeroIndex / 3;
            int zeroX = currentZeroIndex % 3;
            int moveCount = map.get(current);
            for (int d = 0; d < 4; d++) {
                int ny = zeroY + dy[d];
                int nx = zeroX + dx[d];
                if (isOutOfRange(ny, nx)) continue;

                int nextZeroIndex = (ny * 3) + nx;
                String next = getNext(current, nextZeroIndex);
                if (!map.containsKey(next)) {
                    map.put(next, moveCount + 1);
                    q.offer(next);
                }
            }
        }
        System.out.println(-1);
    }

    private static boolean isOutOfRange(int ny, int nx) {
        return 0 > ny || 0 > nx || ny > 2 || nx > 2;
    }

    private static String getNext(String current, int nextZeroIndex) {
        char ch = current.charAt(nextZeroIndex);
        String next = current.replace(ch, 'a');
        next = next.replace('0', ch);
        next = next.replace('a', '0');
        return next;
    }
}
