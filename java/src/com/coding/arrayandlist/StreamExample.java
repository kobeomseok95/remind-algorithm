package com.coding.arrayandlist;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class StreamExample {

    public static void main(String[] args) {
        List<Person> people = new ArrayList<>();
        people.add(new Person(1L, "고범석"));
        people.add(new Person(2L, "김범석"));
        people.add(new Person(3L, "박범석"));

        List<Info> infos = new ArrayList<>();
        infos.add(new Info(3L, 20));
        infos.add(new Info(2L, 21));
        infos.add(new Info(1L, 22));

        List<PersonInfo> personInfos = people.stream()
                .map(person -> {
                    Info findInfo = infos.stream().filter(info -> info.getId().equals(person.getId())).findFirst().orElseThrow();
                    return new PersonInfo(person.getId(), person.getName(), findInfo.getAge());
                })
                .collect(Collectors.toList());
        for (PersonInfo personInfo : personInfos) {
            System.out.println(personInfo.getId() + ", " + personInfo.getName());
        }
    }
}

class Person {
    private Long id;
    private String name;

    public Person(Long id, String name) {
        this.id = id;
        this.name = name;
    }

    public Long getId() {
        return id;
    }

    public String getName() {
        return name;
    }
}

class Info {
    private Long id;
    private int age;

    public Info(Long id, int age) {
        this.id = id;
        this.age = age;
    }

    public Long getId() {
        return id;
    }

    public int getAge() {
        return age;
    }
}

class PersonInfo {
    private Long id;
    private String name;
    private int age;

    public PersonInfo(Long id, String name, int age) {
        this.id = id;
        this.name = name;
        this.age = age;
    }

    public Long getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }
}