class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() < 2)
            return s.length();
        int answer = 0;
        int i = 0;
        int j = 1;
        for (; j < s.length(); j++) {
            for (int k = i; k < j; k++) {
                if (s.charAt(k) == s.charAt(j)) {
                    answer = Math.max(answer, j - i);
                    i = k + 1;
                }
            }
        }
        answer = Math.max(answer, j - i);
        return answer;
    }
}