package com.coding.programmers.level2;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

class Main92335 {

    public int solution(int n, int k) {
        String convertedNumber = convertNumberToString(n, k);
        return countPrimeNumber(convertedNumber);
    }

    private String convertNumberToString(int n, int k) {
        StringBuilder builder = new StringBuilder();
        while (n >= k) {
            builder.append(n % k);
            n /= k;
        }
        if (n != 0) {
            builder.append(n);
        }
        return builder.reverse().toString();
    }

    private int countPrimeNumber(String convertedNumber) {
        int answer = 0;
        List<String> split = Arrays.stream(convertedNumber.split("0"))
                .filter(str -> !str.isBlank())
                .collect(Collectors.toList());
        for (String s : split) {
            if (isPrimeNumber(s)) {
                ++answer;
            }
        }
        return answer;
    }

    private boolean isPrimeNumber(String s) {
        long value = Long.parseUnsignedLong(s);
        if (value == 1) {
            return false;
        }
        boolean prime = true;
        for (int i = 2; i <= Math.sqrt(value); i++) {
            if (value % i == 0) {
                prime = false;
                break;
            }
        }
        return prime;
    }
}
