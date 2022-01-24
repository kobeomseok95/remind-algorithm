package com.coding.arrayandlist;

import java.util.LinkedList;
import java.util.List;

public class LinkedListMain {

    public static void main(String[] args) {
        List<Member> linkedList = new LinkedList<>();
        linkedList.add(new Member("고범석1"));
        linkedList.add(new Member("고범석2"));
        linkedList.add(new Member("고범석3"));
        linkedList.add(new Member("고범석4"));
        linkedList.add(new Member("고범석5"));
        linkedList.add(new Member("고범석6"));
        linkedList.add(new Member("고범석7"));
        linkedList.add(new Member("고범석8"));
        linkedList.add(new Member("고범석9"));
        System.out.println(linkedList.get(1));
    }
}
