'''
给定一个数组，它的第i个元素是一给定股票第i天的价格，如果你最多只允许完成一笔交易，设计获取最大
利润的算法
[7,1,5,3,6,4]
o:5
第2天买入，第5天卖出

[7,6,4,3,1]
o:0

思路：
暴力法

最大利润 = 最高卖出 - 最低买入

'''

def maxProfit(prices):
    minprice = float("inf")
    ans = 0
    for p in prices:  # 买入
        minprice = min(minprice, p) # 最低买入价格
        ans = max(ans, p - minprice)
    return ans


'''
动态规划 做题步骤：
    明确dp(i)应该表示什么
    根据dp(i)和dp(i-1)的关系得出状态转移方程
    确定初始条件，如dp(0)
思路一是由动态规划思想演变而来的 dp(i) = max(dp[i-1],prices[i]-minprice)



'''
def maxProfit2(prices):
    if len(prices) == 0: return 0
    dp = [0] * len(prices)
    minprice = float("inf") # 初始最小无穷大

    for i in range(1, len(prices)):
        minprice = min(minprice, prices[i])
        dp[i] = max(dp[i-1], prices[i] - minprice)

    return dp

print(maxProfit2([7,1,5,3,6,4]))