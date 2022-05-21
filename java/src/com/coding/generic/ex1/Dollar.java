package com.coding.generic.ex1;

public class Dollar extends Money {

    public Dollar(int amount) {
        super(amount);
    }

    @Override
    protected String getAmount() {
        return this.amount + "달러";
    }
}
