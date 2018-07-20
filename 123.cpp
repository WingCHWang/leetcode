int maxProfit(int* prices, int pricesSize) {
    if (pricesSize == 0 || pricesSize == 1)
        return 0;
    int profit_table[pricesSize][pricesSize];
    profit_table[0][1] = prices[1] - prices[0];
    int i = 2;
    int j;
    for(; i<pricesSize; i++) {
        int profit_one_day = prices[i] - prices[i-1];
        profit_table[i-1][i] = profit_one_day;
        
        for(j=1; j<i; j++) {
            profit_table[j][i] = profit_table[i-1][i]+profit_table[j][i-1];
        }
    }
    int max_profit_p[pricesSize][pricesSize];
    int max_profit_n[pricesSize][pricesSize];
    max_profit_p[0][1] = profit_table[0][1];
    for(i=2; i<pricesSize; i++) {
        max_profit_p[0][i] = profit_table[0][i] >  max_profit_p[0][i-1] ? profit_table[0][i] : max_profit_p[0][i-1];
        // max_profit_n[j][pricesSize-i] = profit_table[j][i] >  max_profit_p[j][i-1] ? profit_table[j][i] : max_profit_p[j][i-1];
        
        for(j=1; j<i-1; j++) {
            max_profit_p[j][i] = profit_table[j][i] >  max_profit_p[j][i-1] ? profit_table[j][i] : max_profit_p[j][i-1];
            max_profit_p[j][i] = profit_table[j][i] >  max_profit_p[j-1][i] ? profit_table[j][i] : max_profit_p[j-1][i];        
        }
        max_profit_p[i-1][i] = profit_table[i-1][i] >  max_profit_p[i-2][i] ? profit_table[i-1][i] : max_profit_p[i-2][i];
    }
    max_profit_n[pricesSize-2][pricesSize-1] = profit_table[pricesSize-2][pricesSize-1];
    for(i=pricesSize-3; i >=0 ; i--){
        max_profit_n[i][pricesSize-1] = profit_table[i][pricesSize-1] >  max_profit_n[i+1][pricesSize-1] ? profit_table[i][pricesSize-1] : max_profit_n[i+1][pricesSize-1];
        for(j=pricesSize-2; j>i+1; j--) {
            max_profit_n[i][j] = profit_table[i][j] >  max_profit_n[i+1][j] ? profit_table[i][j] : max_profit_n[i+1][j];
            max_profit_n[i][j] = profit_table[i][j] >  max_profit_n[i][j+1] ? profit_table[i][j] : max_profit_n[i][j+1];
        }
        max_profit_n[i][i+1] = profit_table[i][i+1] >  max_profit_n[i][i+2] ? profit_table[i][i+1] : max_profit_n[i][i+2];

    }
    int max = 0;
    for(j=1; j < pricesSize-1; j++) {
        for(i=0; i< j; i++) {
            int guess = max_profit_p[i][j]+max_profit_n[j][j+1];
            max = guess > max ? guess : max;
        }
    }
    max = max_profit_p[pricesSize-2][pricesSize-1] > max ? max_profit_p[pricesSize-2][pricesSize-1] : max;
    return max;
}