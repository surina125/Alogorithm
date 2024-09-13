const fs = require('fs');
// const readFileSyncAddress = 'input.txt';
const readFileSyncAddress = '/dev/stdin';
const input = fs.readFileSync(readFileSyncAddress).toString().trim().split('\n');

[N,...arr] = input;
N = Number(N);
arr = arr.map(i=>Number(i))


function solution(numbers) {
   numbers.forEach(num => {
      var temp = new Array(90).fill(0);
      var dp=[0,1, 1, 1, 2, 2, 3, 4, 5, 7, 9, ...temp]
      for(let i = 10; i<=num; i++){
         dp[i] = dp[i-1] + dp[i-5]
      }
      console.log(dp[num]);
   });
}

solution(arr)