function processData(input) {
    //Enter your code here
    // input = input.toString(2)
    input = parseInt(input)
    console.log(input, typeof(input))
    input = input.toString(2)
    let wasZero = false;
    master_list = [];
    for (let i = 0; i < input.length; i++) {
        if (input[i] == '0' && !wasZero) {
            master_list.push([]);
            wasZero = true;
        } 
        else if (input[i] == '1') {
            if (master_list.length == 0) {
                master_list.push([]);
            }
            master_list[master_list.length - 1].push(1);
            wasZero = false;
        } 
        else { // (input[i] == '0') as it already was...
            // do nothgin
        }
    }
    
    longest_chain_length = 0;
    for (chain of master_list) {
        if (chain.length > longest_chain_length) {
            longest_chain_length = chain.length;
        }
    }
    // console.log(master_list)
    
    // console.log(2**(longest_chain_length) - 1)
    console.log(longest_chain_length)
} 

// input = '001110001111';
// input = '01010101010100011111111111111111111111111111111111111111111111111111111111111111111111111';
input = "14";

processData(input);