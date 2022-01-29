package com.coding.programmers.level2;

import java.util.*;
import java.util.stream.Collectors;


class Main92341 {

    private static final String DEADLINE_TIME = "23:59";

    public int[] solution(int[] fees, String[] records) {
        Map<String, List<String>> timesPerCar = calculateTimesPerCar(records);
        return calculateFeesPerCar(fees, timesPerCar);
    }

    private Map<String, List<String>> calculateTimesPerCar(String[] records) {
        Map<String, List<String>> rates = new HashMap<>();
        for (String record : records) {
            String[] recordSplit = record.split(" ");
            String time = recordSplit[0];
            String number = recordSplit[1];
            if (!rates.containsKey(number)) {
                rates.put(number, new ArrayList<>());
            }
            rates.get(number).add(time);
        }

        for (String number : rates.keySet()) {
            if (rates.get(number).size() % 2 != 0) {
                rates.get(number).add(DEADLINE_TIME);
            }
        }
        return rates;
    }

    private int[] calculateFeesPerCar(int[] fees, Map<String, List<String>> timesPerCar) {
        int[] answer = new int [timesPerCar.size()];
        int index = 0;
        for (String key : timesPerCar.keySet().stream().sorted().collect(Collectors.toList())) {
            List<String> times = timesPerCar.get(key);
            int minutes = getAllMinutes(times);
            answer[index] = calculateFee(fees, minutes);
            ++index;
        }
        return answer;
    }

    private int getAllMinutes(List<String> times) {
        int allMinutes = 0;
        for (int i = 0; i < times.size(); i += 2) {
            String[] t1 = times.get(i).split(":");
            String[] t2 = times.get(i + 1).split(":");
            int hours = Integer.parseInt(t2[0]) - Integer.parseInt(t1[0]);
            int minutes = 0;
            if (Integer.parseInt(t2[1]) > Integer.parseInt(t1[1])) {
                hours -= 1;
                minutes = Integer.parseInt(t2[1]) - Integer.parseInt(t1[1]) + 60;
            } else {
                minutes = Integer.parseInt(t2[1]) - Integer.parseInt(t1[1]);
            }
            allMinutes += hours * 60 + minutes;
        }
        return allMinutes;
    }

    private int calculateFee(int[] fees, int minutes) {
        int defaultMinutes = fees[0];
        int defaultFees = fees[1];
        int billingMinutes = fees[2];
        int billingFees = fees[3];

        if (minutes <= defaultMinutes) {
            return defaultFees;
        }
        int ceil = (int) Math.ceil((double) (minutes - defaultMinutes) / billingMinutes);
        return defaultFees + (ceil * billingFees);
    }
}
