function processData(input) {
    //Enter your code here
    // input = input.split(",")
    input = [1, 55, 34, 1, 44]
    
    for (let i = 0; i<input.length; i++) {
        input[i] = parseInt(input[i])
    }
    
    // find 4 plus grands nombres ds liste
    i_value = 0;
    n_value = 0;
    f_value = 0;
    o_value = 0;
    
    allPossibleDifferences = []

    for (let i = 0; i < input.length - 1; i++) {
        for (let j  = i + 1; j < input.length; j++) {
            if (input[j] > input[i] && (input.length - (j-i) > 2)) {
                allPossibleDifferences.push([[j, input[j]], [i, input[i]]]);
            }
        }
    }

    allPossibleDifferences.sort((kv_pairs1, kv_pairs2) => {
        return (kv_pairs1[0][1] - kv_pairs1[1][1]) - (kv_pairs2[0][1] - kv_pairs2[1][1]);
    });

    allPossibleDifferences.reverse();
    // console.log(allPossibleDifferences)

    let differenceTotal = 0;
    let firstTerm = [];
    let secondTerm = [];
    for (const [index, val] of allPossibleDifferences.entries()) {
        tempTotalDifference = val[0][1] - val[1][1];
        tempTotalDifference2 = 0;
        tempSecondTerm = []
        for (let j = index + 1; j<allPossibleDifferences.length; j++) {
            let currentDifference = allPossibleDifferences[j][0][1] - allPossibleDifferences[j][1][1];
            let areIndexesOk = 
                (val[1][0] > allPossibleDifferences[j][0][0] || val[0][0] < allPossibleDifferences[j][1][0]);
            if (currentDifference > tempTotalDifference2 && areIndexesOk) {
                tempTotalDifference2 = currentDifference;
                tempSecondTerm = allPossibleDifferences[j];
            }
        }
        tempTotalDifference += tempTotalDifference2;
        if (tempTotalDifference > differenceTotal) {
            differenceTotal = tempTotalDifference;
            firstTerm = val;
            secondTerm = tempSecondTerm;
        }
    }
    // console.log("differenceTotal", differenceTotal)
    // console.log("firstTerm", firstTerm)
    // console.log("secondTerm", secondTerm)
    console.log(firstTerm[0][1] - firstTerm[1][1] + secondTerm[0][1] - secondTerm[1][1])

} 

processData();