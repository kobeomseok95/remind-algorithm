package programmers.level2

class Solution {
    fun solution(s: String) = (1..s.length).map { compress(s, it) }.minOf { it }

    private fun compress(s: String, n: Int): Int {
        val countStringPairs = ArrayList<Pair<Int, String>>()
        s.chunked(n).forEach { chunkedStr ->
            if (countStringPairs.isEmpty()) {
                countStringPairs.add(1 to chunkedStr)
            } else {
                val pair = countStringPairs.last()
                if (pair.second == chunkedStr) {
                    countStringPairs.removeAt(countStringPairs.lastIndex)
                    countStringPairs.add(pair.first + 1 to chunkedStr)
                } else {
                    countStringPairs.add(1 to chunkedStr)
                }
            }
        }
        return countStringPairs.fold(0) { sum, pair ->
            sum + pair.second.length + if (pair.first <= 1) 0 else pair.first.toString().length
        }
    }
}


fun main() {
    val s = Solution()
    println(s.solution("aabbaccc"))                 // 7
    println(s.solution("ababcdcdababcdcd"))         // 9
    println(s.solution("abcabcdede"))               // 8
    println(s.solution("abcabcabcabcdededededede")) // 14
    println(s.solution("xababcdcdababcdcd"))        // 17
    println(s.solution("aaaaaaaaaaaabcd"))          // 6
    println(s.solution("xxxxxxxxxxyyy"))            // 5
}