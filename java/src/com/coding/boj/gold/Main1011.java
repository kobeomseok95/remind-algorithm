package com.coding.boj.gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main1011 {

    private static final BufferedReader READER = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int t = Integer.parseInt(READER.readLine());
        for (int i = 0; i < t; i++) {
            System.out.println(solve());
        }
    }

    private static int solve() throws IOException {
        String[] xy = READER.readLine().split(" ");
        int distance = Integer.parseInt(xy[1]) - Integer.parseInt(xy[0]);
        int max = (int) Math.sqrt(distance);
        if (max == Math.sqrt(distance)) {
            return 2 * max - 1;
        } else if (max * max < distance && distance <= max * max + max) {
            return 2 * max;
        } else {
            return 2 * max + 1;
        }
    }
}
