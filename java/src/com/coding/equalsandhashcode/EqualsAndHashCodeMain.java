package com.coding.equalsandhashcode;

import java.util.HashSet;
import java.util.Set;

public class EqualsAndHashCodeMain {
    public static void main(String[] args) {
        Member member1 = new Member(1L, "고범석");
        Member member2 = new Member(1L, "고범석");
        Set<Member> set = new HashSet<>();
        set.add(member1);
        set.add(member2);
        System.out.println(set.size());
    }
}
