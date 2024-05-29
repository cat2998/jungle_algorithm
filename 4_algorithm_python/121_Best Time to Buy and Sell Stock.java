class Solution {
    public int maxProfit(int[] prices) {
        int[] dp = new int[prices.length];
        for (int i = 1; i < prices.length; i++) {
            if (prices[i - 1] < prices[i] && dp[i - 1] < prices[i]) {
                int buy = prices[0];
                for (int j = 1; j < i; j++) {
                    if (buy > prices[j])
                        buy = prices[j];
                }
                dp[i] = Math.max(dp[i - 1], buy * (-1) + prices[i]);
            } else
                dp[i] = dp[i - 1];
        }
        return dp[prices.length - 1];
    }
}