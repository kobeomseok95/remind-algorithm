package com.coding.equalsandhashcode;

import java.util.Objects;

public class Member {

    private Long id;
    private String name;

    public Member(Long id, String name) {
        this.id = id;
        this.name = name;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Member)) return false;
        Member member = (Member) o;
        return id.equals(member.id) && name.equals(member.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, name);
    }
}
