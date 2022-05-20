package com.coding.arrayandlist;

import java.util.ArrayList;
import java.util.List;

public class ArrayAndList {

    public static void main(String[] args) {
        Member test1 = new Member("test1");
        Member test2 = new Member("test2");
        Member test3 = new Member("test3");

        List<Member> memberList = new ArrayList<>();
        memberList.add(test1);
        memberList.add(test2);
        memberList.add(test3);

        Member[] memberArray = new Member[3];
        memberArray[0] = test1;
        memberArray[1] = test2;
        memberArray[2] = test3;
    }
}
