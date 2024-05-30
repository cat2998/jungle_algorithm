class Solution {
    public int reverse(int x) {
        boolean minus = false;
        String str = "";
        int answer;
        if (x == 0)
            return x;
        if (x < 0)
            minus = true;
        while (x != 0) {
            str += Integer.toString(Math.abs(x % 10));
            x /= 10;
        }
        if (Math.pow(2, 31) < Long.parseLong(str))
            return 0;
        if (minus)
            answer = (-1) * Integer.parseInt(str);
        else
            answer = Integer.parseInt(str);
        return answer;
    }
}