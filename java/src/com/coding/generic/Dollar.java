package com.coding.generic;

public class Dollar extends Money {

    public Dollar(int amount) {
        super(amount);
    }

    @Override
    protected String getAmount() {
        return this.amount + "달러";
    }
}
