package com.coding.boj.gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main1339 {

    private static final BufferedReader READER = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        System.out.println(solve());
    }

    private static int solve() throws IOException {
        String[] words = init();
        int[] frequency = getSortedAlphabetFrequency(words);
        return calculateWordMaxValue(frequency);
    }

    private static String[] init() throws IOException {
        int wordCount = Integer.parseInt(READER.readLine());
        String[] words = new String[wordCount];
        for (int i = 0; i < wordCount; i++) {
            words[i] = READER.readLine();
        }
        return words;
    }

    private static int[] getSortedAlphabetFrequency(String[] words) {
        int[] frequency = new int[26];
        for (String word : words) {
            int weight = (int) Math.pow(10, word.length() - 1);
            for (int i = 0; i < word.length(); i++) {
                frequency[(int) word.charAt(i) - 65] += weight;
                weight /= 10;
            }
        }
        Arrays.sort(frequency);
        return frequency;
    }

    private static int calculateWordMaxValue(int[] frequency) {
        int index = 9;
        int sum = 0;
        for (int i = frequency.length - 1; i >= 0; i--) {
            if (frequency[i] == 0) {
                break;
            }
            sum += frequency[i] * index;
            --index;
        }
        return sum;
    }
}
