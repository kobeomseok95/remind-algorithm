package com.coding.generic.ex1;

import java.util.List;

public class MoneyPrinter {

    public void print(List<? extends Money> moneyList) {
        moneyList.forEach(it ->
                System.out.println(it.getAmount())
        );
    }
}
