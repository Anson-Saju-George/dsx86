
# x is cost of coupon
# prices is list of prices
# y is discount
# if cost - discount < 0 then 0 else cost - discount
# Output "COUPON" if sum of all discounted prices < sum of original prices else "NO COUPON"
x = 1000
prices = [100, 200, 300, 400, 500]
y = 150
Red_List = [a-y if a-y > 0 else 0 for a in prices]

class Solution:
    def check_coupon(self, n, x, y, prices):
        # write your code here
        Sum = sum(prices)
        Red_List = [a-y if a-y > 0 else 0 for a in prices]
        # print(Sum,Red_List,sum(Red_List))
        if sum(Red_List)+x < Sum:
            return "COUPON"
        else:
            return "NO COUPON"

# Example usage
sol = Solution()
result = sol.check_coupon(5, 1000, 150, [100, 200, 300, 400, 500])
print(result)  # Output: