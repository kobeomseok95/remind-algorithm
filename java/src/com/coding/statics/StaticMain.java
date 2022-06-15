package com.coding.statics;

public class StaticMain {
    public static void main(String[] args) {
        StaticSample sample = new StaticSample("anotherName");
        System.out.println(System.identityHashCode(StaticSample.staticName));
        System.out.println(System.identityHashCode(StaticSample.integer));

        sample.change();
        System.out.println(System.identityHashCode(StaticSample.staticName));
        System.out.println(System.identityHashCode(StaticSample.integer));
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
