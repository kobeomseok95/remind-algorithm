package com.coding.boj.gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

class Main2250 {

    static class Node {
        private int parentNumber;
        private int number;
        private int leftNumber;
        private int rightNumber;

        public Node(int number, int leftNumber, int rightNumber) {
            this.parentNumber = -1;
            this.number = number;
            this.leftNumber = leftNumber;
            this.rightNumber = rightNumber;
        }

        public void setLeftNumber(int left) {
            this.leftNumber = left;
        }

        public void setRightNumber(int right) {
            this.rightNumber = right;
        }

        public void setParent(int parent) {
            this.parentNumber = parent;
        }

        public boolean isRoot() {
            return this.parentNumber == -1;
        }
    }

    private static final BufferedReader READER = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer tokenizer;
    private static int N;
    private static int[] minWidth;
    private static int[] maxWidth;
    private static List<Node> tree = new ArrayList<>();
    private static int maxLevel = 0;
    private static int x = 1;

    public static void main(String[] args) throws IOException {
        init();
        setUpTree();
        int root = findRoot();
        inOrder(root, 1);
        int answerLevel = 0;
        int widthDifference = 0;
        for (int level = 1; level <= maxLevel; level++) {
            if (widthDifference < Math.abs(maxWidth[level] - minWidth[level]) + 1) {
                widthDifference = Math.abs(maxWidth[level] - minWidth[level]) + 1;
                answerLevel = level;
            }
        }
        System.out.println(answerLevel + " " + widthDifference);
    }

    private static void init() throws IOException {
        N = Integer.parseInt(READER.readLine());
        minWidth = new int[N + 1];
        for (int i = 0; i <= N; i++) {
            minWidth[i] = N + 1;
        }
        maxWidth = new int[N + 1];
    }

    private static void setUpTree() throws IOException {
        for (int i = 0; i <= N; i++) {
            tree.add(new Node(i, -1, -1));
        }

        for (int i = 0; i < N; i++) {
            tokenizer = new StringTokenizer(READER.readLine());
            int current = Integer.parseInt(tokenizer.nextToken());
            int left = Integer.parseInt(tokenizer.nextToken());
            int right = Integer.parseInt(tokenizer.nextToken());
            tree.get(current).setLeftNumber(left);
            tree.get(current).setRightNumber(right);
            if (left != -1) {
                tree.get(left).setParent(current);
            }
            if (right != -1) {
                tree.get(right).setParent(current);
            }
        }
    }

    private static int findRoot() {
        int root = 1;
        for (int i = 1; i <= N; i++) {
            if (tree.get(i).isRoot()) {
                return tree.get(i).number;
            }
        }
        return root;
    }

    private static void inOrder(int nodeNumber, int level) {
        if (tree.get(nodeNumber).leftNumber != -1) {
            inOrder(tree.get(nodeNumber).leftNumber, level + 1);
        }
        if (maxLevel < level) {
            maxLevel = level;
        }
        minWidth[level] = Math.min(minWidth[level], x);
        maxWidth[level] = x;
        ++x;
        if (tree.get(nodeNumber).rightNumber != -1) {
            inOrder(tree.get(nodeNumber).rightNumber, level + 1);
        }
    }
}
