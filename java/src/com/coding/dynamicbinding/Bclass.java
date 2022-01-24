package com.coding.dynamicbinding;

public class Bclass extends Aclass {

    @Override
    public void out() {
        System.out.println("B class");
    }

    public static void staticMethod() {
        System.out.println("B class Static method");
    }
}
