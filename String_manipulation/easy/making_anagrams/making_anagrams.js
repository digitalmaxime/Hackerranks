const fs = require('fs')

function makeAnagram(a, b) {
    // Write your code here
    let alphabetA = Array(26).fill(0);
    let alphabetB = Array(26).fill(0);
    
    for (let i = 0; i < a.length; i++) {
        alphabetA[a.charCodeAt(i) - 97]++;
    }
    
    for (let i = 0; i < b.length; i++) {
        alphabetB[b.charCodeAt(i) - 97]++;
    }
    
    let result = 0;
    for (let i = 0; i < 26; i++) {
        const temp = Math.abs(alphabetA[i] - alphabetB[i]);
        result += temp;
    }
    
    return result
    
}

const a = "abcdef";

const b = "abcde";


const res = makeAnagram(a, b);
console.log(res)
