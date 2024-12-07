class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        for (int i = 0; i < prices.length - 1; i++) {
            int todaysPrice = prices[i];
            int subArrayLength = (prices.length - 1) - i;
            int[] remainingPrices = Arrays.copyOfRange(prices, i, prices.length);
            for (int j = 0; j < remainingPrices.length; j++) {
                int profit = remainingPrices[j] - todaysPrice;
                if (profit > maxProfit) {
                    maxProfit = profit;
                }
            }
        }
        return maxProfit;   
    }
}