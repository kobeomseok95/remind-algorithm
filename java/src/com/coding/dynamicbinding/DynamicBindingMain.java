package com.coding.dynamicbinding;

import java.util.ArrayList;

public class DynamicBindingMain {

    public static void main(String[] args) {
        ArrayList<Aclass> list = new ArrayList<>();
        list.add(new Aclass());
        list.add(new Bclass());
        list.add(new Cclass());
        for (Aclass abc : list) {
            abc.staticMethod();
        }
    }
}
