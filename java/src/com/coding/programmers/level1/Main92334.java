package com.coding.programmers.level1;

import java.util.*;
import java.util.stream.Collectors;

class Main92334 {

    public int[] solution(String[] idList, String[] reports, int k) {
        List<String> list = Arrays.stream(reports).distinct().collect(Collectors.toList());
        HashMap<String, Integer> countMap = new HashMap<>();
        for (String s : list) {
            String target = s.split(" ")[1];
            countMap.put(target, countMap.getOrDefault(target, 0) + 1);
        }

        return Arrays.stream(idList).map(user -> {
            List<String> reportList = list.stream().filter(s -> s.startsWith(user + " ")).collect(Collectors.toList());
            return reportList.stream().filter(s -> countMap.getOrDefault(s.split(" ")[1], 0) >= k).count();
        }).mapToInt(Long::intValue).toArray();
    }
}
