function substrCount(n, s) {
    let res = 0;
    
    for (let i = 0; i < s.length; i++) {
        let j = 1;    
        let sameChar = s[i-1] || -1;
        while (i-j >= 0 && i+j < s.length && s[i-j] == sameChar && s[i+j] == sameChar) {
            res ++;
            j ++;
        }
    }
    
    for (let i = 0; i < s.length; i++) {
        let j = 1;        
        while (i + j < s.length && s[i+j] == s[i]) {
            if (j % 2 == 1) {
                res ++;
            }
            j++
        }
    }

    return res + n;
}

console.log(substrCount(7, 'abcbaba'))
// console.log(substrCount(4, 'aaaa'))
