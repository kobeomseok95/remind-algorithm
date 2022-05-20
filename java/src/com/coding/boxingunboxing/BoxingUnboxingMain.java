package com.coding.boxingunboxing;

public class BoxingUnboxingMain {
    public static void main(String[] args) {
        Integer i1 = Integer.valueOf(1);
        Integer i2 = Integer.valueOf(1);
        System.out.println("i1 == i2 : " + (i1 == i2));
        System.out.println("i1.equals(i2) : " + i1.equals(i2));
    }
}
