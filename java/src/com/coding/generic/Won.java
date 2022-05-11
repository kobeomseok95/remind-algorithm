package com.coding.generic;

public class Won extends Money {

    public Won(int amount) {
        super(amount);
    }

    @Override
    protected String getAmount() {
        return this.amount + "원";
    }
}
