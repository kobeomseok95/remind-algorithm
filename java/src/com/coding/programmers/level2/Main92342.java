package com.coding.programmers.level2;


class Main92342 {

    private int n;
    private int[] apeachScoreTable;
    private int[] ryanScoreTable = new int[11];
    private int maxScore = 0;
    private int[] answer = {-1};


    public int[] solution(int n, int[] info) {
        this.apeachScoreTable = info;
        this.n = n;

        dfs(true, 10, 0);
        dfs(false, 10, 0);

        return answer;
    }

    private void dfs(boolean isRyanWin, int targetScore, int ryanScore) {
        if (targetScore < 0) {
            calculateScore();
            return;
        }

        if (!isRyanWin) {
            dfs(true, targetScore - 1, ryanScore);
            dfs(false, targetScore - 1, ryanScore);
            return;
        }

        int needWinShotCount = apeachScoreTable[targetScore] + 1;
        if (n >= needWinShotCount) {
            n -= needWinShotCount;
            ryanScoreTable[targetScore] = needWinShotCount;
            dfs(true, targetScore - 1, ryanScore + targetScore);
            dfs(false, targetScore - 1, ryanScore + targetScore);
            ryanScoreTable[targetScore] = 0;
            n += needWinShotCount;
        }
    }

    private void calculateScore() {
        int apeachScore = 0;
        int ryanScore = 0;
        for (int i = 0; i <= 10; i++) {
            if (apeachScoreTable[i] == 0 && ryanScoreTable[i] == 0)
                continue;

            if (apeachScoreTable[i] >= ryanScoreTable[i]) {
                apeachScore += (10 - i);
            } else {
                ryanScore += (10 - i);
            }
        }

        if (ryanScore > apeachScore && (ryanScore - apeachScore) > maxScore) {
            maxScore = (ryanScore - apeachScore);
            answer = new int[11];
            for (int i = 0; i <= 10; i++) {
                answer[i] = ryanScoreTable[i];
            }
            if (n != 0) {
                answer[10] += n;
            }
        }
        return ;
    }
}
