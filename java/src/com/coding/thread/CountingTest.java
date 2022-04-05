package com.coding.thread;

import java.util.HashSet;
import java.util.Set;
import java.util.concurrent.atomic.AtomicInteger;

public class CountingTest {

    public static void main(String[] args) {
        Count count = new Count();
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < 100; i++) {
            new Thread(){
                public void run(){
                    for (int j = 0; j < 100; j++) {
                        set.add(count.view());
                    }
                }
            }.start();
        }
        try {
            Thread.sleep(5000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println(set.size());
    }
}

class Count {
    private AtomicInteger count = new AtomicInteger(0);
    public synchronized int view() {return count.getAndIncrement();}
}
