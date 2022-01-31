package com.coding.programmers.level3;

import java.util.*;

class Main92343 {

    private int answer = 0;
    private int[] info;
    private Map<Integer, ArrayList<Integer>> tree;

    public int solution(int[] info, int[][] edges) {
        init(info, edges);
        List<Integer> shouldVisitPoints = new ArrayList<>();
        shouldVisitPoints.add(0);
        dfs(0, 0, 0, shouldVisitPoints);
        return answer;
    }

    private void init(int[] info, int[][] edges) {
        this.info = info;
        this.tree = makeTree(edges);
        this.answer = 0;
    }

    private Map<Integer, ArrayList<Integer>> makeTree(int[][] edges) {
        Map<Integer, ArrayList<Integer>> map = new HashMap<>();
        for (int[] edge : edges) {
            int parent = edge[0];
            int child = edge[1];
            if (!map.containsKey(parent)) {
                map.put(parent, new ArrayList<>());
            }
            map.get(parent).add(child);
        }
        return map;
    }

    private void dfs(int node, int sheep, int wolf, List<Integer> shouldVisitNodes) {
        if (info[node] == 0)
            ++sheep;
        else
            ++wolf;
        if (wolf >= sheep)
            return;

        answer = Math.max(answer, sheep);

        List<Integer> nextVisitNodes = getNextVisitNodes(node, shouldVisitNodes);
        for (int nextNode : nextVisitNodes) {
            dfs(nextNode, sheep, wolf, nextVisitNodes);
        }
    }

    private List<Integer> getNextVisitNodes(int node, List<Integer> shouldVisitNodes) {
        List<Integer> next = new ArrayList<>(shouldVisitNodes);
        if (tree.containsKey(node)) {
            next.addAll(tree.get(node));
        }
        next.remove(Integer.valueOf(node));
        return next;
    }
}
