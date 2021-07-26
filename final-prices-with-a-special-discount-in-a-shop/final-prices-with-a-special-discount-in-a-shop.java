class Solution {
    public int[] finalPrices(int[] prices) {
        int n = prices.length;
        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            int p = prices[i];
            res[i] = p;
            for (int j = i + 1; j < n; j++) {
                if (prices[j] <= prices[i]) {
                    res[i] -= prices[j];
                    break;
                }
            }
        }
        return res;
    }
}