## Problem

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

## Solution
做法，把這個數字除以第一個 `prime number`, 一直到無法整除，接下來除以第二個 `prime number...` 一次類推，一直到最後剩下的數字也是 `prime number` 爲止

要考慮到不要一直重複的檢查某個數字是否爲prime, 只要有檢查過，就需要把 `prime` 記下來。這樣之後再使用就可用O(1) 的時間來判斷是否是 `prime`