function processData(input) {
    //Enter your code here
    num = parseInt(input, 2);
    console.log(num)
    // if (num.isalpha)
    if (num % 7 == 0) {
        console.log('True');
        // return true;
    }
    else {
        console.log('False..')
    }
} 

input = '';

processData(input);