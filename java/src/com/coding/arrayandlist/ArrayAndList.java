package com.coding.arrayandlist;

import java.util.ArrayList;
import java.util.List;

public class ArrayAndList {

    public static void main(String[] args) {
        Member member1 = new Member("고범석1", "01012341234");
        Member member2 = new Member("고범석2", "01012341235");
        List<Member> list = new ArrayList<>();
        list.add(member1);
        list.add(member2);
        System.out.println("==== 리스트");
        for (int i = 0; i < 2; i++) {
            System.out.println(list.get(i));
        }

        Member[] array = new Member[] {
                member1,
                member2
        };
        System.out.println("==== 배열");
        for (int i = 0; i < 2; i++) {
            System.out.println(array[i]);
        }
        Member[] members = new Member[3];
        members[0] = member1;
        members[1] = member2;
        System.out.println(members.length);

    }
}
