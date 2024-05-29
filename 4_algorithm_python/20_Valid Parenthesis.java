class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for (int i = 0 ; i < s.length(); i++) {
            if (s.charAt(i) == '(' || s.charAt(i) == '{' || s.charAt(i) == '[')
                stack.push(s.charAt(i));
            else {
                if (stack.empty())
                    return false;
                char pop = stack.pop();
                if (pop == '(' && s.charAt(i) != ')')
                    return false;
                else if (pop == '{' && s.charAt(i) != '}')
                    return false;
                else if (pop == '[' && s.charAt(i) != ']')
                    return false;
            }
        }
        if (!stack.empty())
            return false;
        return true;
    }
}