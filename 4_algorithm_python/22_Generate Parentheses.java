class Solution {
    public List<String> generateParenthesis(int n) {
        String str = "";
        List<String> list = new ArrayList<>();
        makePattern(list, str, '(', n * 2 - 1, 0);
        return list;
    }
    public void makePattern(List<String> list, String str, char pattern, int n, int depth) {
        str += pattern;
        if (n == depth) {
            Stack<Character> stack = new Stack<>();
            for (int i = 0; i < str.length(); i++) {
                if (str.charAt(i) == '(')
                    stack.push('(');
                else {
                    if (stack.empty())
                        return;
                    stack.pop();
                }
            }
            if (stack.empty())
                list.add(str);
            return;
        }
        makePattern(list, str, '(', n, depth + 1);
        makePattern(list, str, ')', n, depth + 1);
    }
}