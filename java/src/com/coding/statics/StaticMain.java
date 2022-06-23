package com.coding.statics;

public class StaticMain {
    public static void main(String[] args) {

    }
}

class StaticSample {
    static int integer = 10;
    static String staticName = "staticName";
    String anotherName;

    public StaticSample(String anotherName) {
        this.anotherName = anotherName;
    }

    public void change() {
        integer = 20;
        staticName = "asdf";
    }
}
