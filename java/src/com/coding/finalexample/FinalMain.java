package com.coding.finalexample;

public class FinalMain {

    static final int a = 20;
    static final Sample sample = new Sample(10, "테스트");

    public static void main(String[] args) {
//        a = 10;
        sample.setCode(20);
        sample.setName("수정");
        System.out.println(sample);
//        sample = new Sample(10, "asdf");
    }
}
