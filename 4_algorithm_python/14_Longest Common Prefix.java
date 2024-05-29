class Solution {
    public String longestCommonPrefix(String[] strs) {
        String answer = "";
        boolean flag;
        for (int i = 0; i < strs[0].length(); i++) {
            flag = true;
            for (int j = 1; j < strs.length; j++) {
                if (strs[j].length() <= i || strs[0].charAt(i) != strs[j].charAt(i)) {
                    flag = false;
                    break;
                }
            }
            if (flag)
                answer += strs[0].charAt(i);
            else
                break;
        }
        return answer;
    }
}