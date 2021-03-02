# A Dynamic Programming based Python

def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
 
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]
                          + K[i-1][w-wt[i-1]],  
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
 
    return K[n][W],K
 
# Driver code
val = [9, 7, 3, 3, 11, 4]
wt = [5, 5, 2, 3, 6, 3]
W = 14

n = len(val)
optimal_val,table = knapSack(W, wt, val, n)
print("optimal_val",optimal_val)
for i in range(1,len(val)+1):
 for j in range(W+1):
  print(table[i][j],end="\t")
 print()