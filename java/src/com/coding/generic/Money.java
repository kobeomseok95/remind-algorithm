package com.coding.generic;

public abstract class Money {
    protected int amount;
    protected abstract String getAmount();

    public Money(int amount) {
        this.amount = amount;
    }
}
