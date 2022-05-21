package com.coding.generic.ex1;

public class Won extends Money {

    public Won(int amount) {
        super(amount);
    }

    @Override
    protected String getAmount() {
        return this.amount + "원";
    }
}
