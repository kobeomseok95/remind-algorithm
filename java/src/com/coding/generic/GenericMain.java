package com.coding.generic;

import java.util.List;

public class GenericMain {

    public static void main(String[] args) {
        Won 백원 = new Won(100);
        Dollar 사달러 = new Dollar(4);
        MoneyPrinter.print(List.of(백원, 사달러));
    }
}
