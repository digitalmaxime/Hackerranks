function processData(input) {
    //Enter your code here
    // console.log(input)
    input = input.split(" ");
    a = input[0];
    b = input[1];
    if (a == 0) {
        console.log(b)
        return b;
    }
    
    newA = b % a;
    newB = a;
    newInput = newA.toString().concat(" ").concat(newB.toString())

    return processData(newInput);
} 

processData("12 8")