package com.coding.generic;

import java.util.List;

public class MoneyPrinter {

    public static void print(List<? extends Money> moneyList) {
        moneyList.forEach(it ->
                System.out.println(it.getAmount())
        );
    }
}
