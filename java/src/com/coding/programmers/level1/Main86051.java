package com.coding.programmers.level1;

import java.util.Arrays;
import java.util.stream.IntStream;

class Main86051 {

    public int solution(int[] numbers) {
        return IntStream.rangeClosed(0, 9)
                .filter(i -> Arrays.stream(numbers)
                        .noneMatch(num -> num == i))
                .sum();
    }
}
