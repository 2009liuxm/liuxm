i = 0
total = 500000.0
interest_tuple = (0.01, 0.02, 0.03, 0.035)
repay = 30000.0
while total > 0:
      i = i + 1
      if i < 5:
         total = total*(1+interest_tuple[i-1])-repay
      else:
         total = total*1.05-repay
print(i+1)
