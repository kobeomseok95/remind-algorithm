package com.coding.generic.ex2;

import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.Stack;

public class Generic2Main {
    public static void main(String[] args) {
        Stack<Mammal> cage = new Stack<>();
        Collection<Cat> cats = Arrays.asList(
                new Cat(),
                new Cat()
        );
        for (Cat cat : cats) {
            cage.push(cat);
        }

        Collection<Animal> shelter = Collections.emptyList();
        shelter.addAll(cage);
    }
}
