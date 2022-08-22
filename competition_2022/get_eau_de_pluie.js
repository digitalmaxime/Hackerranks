function processData(input) {
    let res = 0;
    let currentMaxHeightToResolve = input[0]
    let maybePile = []
    for (let i = 1; i < input.length; i++) {
        if (input[i] < currentMaxHeightToResolve) {
            maybePile.push(input[i]);
        } else {
            maybePile.forEach((ele) => { 
                res += currentMaxHeightToResolve - ele; 
            })
            maybePile = [];
            tempNextLimitingMax = 0;
            for (let j = i + 1; j < input.length; j++) {
                if (input[j] > tempNextLimitingMax) {
                    tempNextLimitingMax = input[j];
                }
            }
            currentMaxHeightToResolve = Math.min(tempNextLimitingMax, input[i]);
        } 
    }
    
    console.log(res);
} 

processData([2,0,3,5,4,1,2,3,0,2])
//             2       2 1   2 
// processData([2,2,3,4,3,1,2,3,0,2])
//                     2 1 0 2