package com.coding.callbyvaluereference;

public class CallByValueMain {
    public static void main(String[] args) {
        method();
    }

    private static void method() {
        Person person = new Person(20, "고범석");
        System.out.println(System.identityHashCode(person));
        System.out.println("Before call, age = " + person.age + ", name = " + person.name);
        call(person);
        System.out.println(System.identityHashCode(person));
        System.out.println("After call, age = " + person.age + ", name = " + person.name);

//        int a = 10;
//        int b = 20;
//        System.out.println("Before a : " + System.identityHashCode(a));
//        System.out.println("Before b : " + System.identityHashCode(b));
//        System.out.println("Before a : " + a);
//        System.out.println("Before b : " + b);
//        call(a, b);
//        System.out.println("After a : " + System.identityHashCode(a));
//        System.out.println("After b : " + System.identityHashCode(b));
//        System.out.println("Before a : " + a);
//        System.out.println("Before b : " + b);
//        System.out.println(System.identityHashCode(person));
//        System.out.println("After call, age = " + person.age + ", name = " + person.name);
    }

    private static void call(Person a) {
//        aa = 40;
//        bb = 50;
//        System.out.println("Inside aa : " + System.identityHashCode(aa));
//        System.out.println("Inside bb : " + System.identityHashCode(bb));
//        System.out.println("Inside aa : " + aa);
//        System.out.println("Inside bb : " + bb);
        System.out.println(System.identityHashCode(a));
        a.age = 30;
        a.name = "김범석";
        System.out.println("call, age = " + a.age + ", name = " + a.name);
    }
}

class Person {
    int age;
    String name;

    public Person(int age, String name) {
        this.age = age;
        this.name = name;
    }
}