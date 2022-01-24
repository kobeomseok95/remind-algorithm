package com.coding.dynamicbinding;

public class Cclass extends Aclass {

    @Override
    public void out() {
        System.out.println("C class");
    }

    public static void staticMethod() {
        System.out.println("C class Static method");
    }
}
