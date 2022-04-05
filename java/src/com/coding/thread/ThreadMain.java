package com.coding.thread;

import java.io.IOException;

public class ThreadMain {

    static long startTime = 0;

    private static void singleThread() {
        long startTime = System.currentTimeMillis();
        for (int i = 0; i < 300; i++) {
            System.out.printf("%s", new String("-"));
        }
        System.out.println("소요시간 1 : " + (System.currentTimeMillis() - startTime));

        for (int i = 0; i < 300; i++) {
            System.out.printf("%s", new String("|"));
        }
        System.out.println("소요시간 2 : " + (System.currentTimeMillis() - startTime));
    }

    public static void main(String[] args) throws IOException {
        ThreadGroup group = Thread.currentThread().getThreadGroup();
        ThreadGroup newGroup1 = new ThreadGroup("new Group1");
        ThreadGroup newGroup2 = new ThreadGroup("new Group2");

        ThreadGroup newSubGroup1 = new ThreadGroup(newGroup1, "new Sub Group1");
        newGroup1.setMaxPriority(2);
        Runnable runnable = () -> {
            try {
                System.out.println(Thread.currentThread().getName() + " 호출");
                Thread.sleep(1000);
                System.out.println("===============");
                System.out.println(Thread.currentThread().getName() + " 종료");
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        };

        new Thread(newGroup1, runnable, "t1").start();
        new Thread(newGroup2, runnable, "t3").start();
        new Thread(newSubGroup1, runnable, "t2").start();
//        System.out.println(
//                ">> List of ThreadGroup : " + group.getName()
//                + ", Active ThreadGroup : " + group.activeGroupCount()
//                + ", Active Thread : " + group.activeCount()
//        );
        group.list();
    }
}

class MultiThread extends Thread {

    @Override
    public void run() {
        for (int i = 0; i < 10; i++) {
            System.out.println(i + 1);
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}