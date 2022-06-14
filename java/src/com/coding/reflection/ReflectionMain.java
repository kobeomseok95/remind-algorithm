package com.coding.reflection;

import java.lang.reflect.Method;

public class ReflectionMain {
    public static void main(String[] args) throws Exception {
        Object obj = new User(1L, "고범석");
        Class<User> userClass = User.class;
        Method[] methods = userClass.getMethods();
        for (Method method : methods) {
            method.invoke(obj);
        }
    }
}

class User {
    private Long id;
    private String username;

    public User(Long id, String username) {
        this.id = id;
        this.username = username;
    }

    public void printMyId() {
        System.out.println(id);
    }

    public void printMyUsername() {
        System.out.println(username);
    }
}