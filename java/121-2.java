class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        for (int i = 0; i < prices.length - 1; i++) {
            int todaysPrice = prices[i];
            int remainingPricesLength = (prices.length) - i;
            int[] remainingPrices = new int[remainingPricesLength];  
            System.arraycopy(prices, i, remainingPrices, 0, remainingPricesLength);
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