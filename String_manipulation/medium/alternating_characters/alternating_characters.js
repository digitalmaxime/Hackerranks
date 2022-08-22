function alternatingCharacters(s) {
    // Write your code here
    if (s.length == 0) {
        return 0;
    }
    
    let previousChar = s[0];
    let result = 0;
    
    for (let i = 1; i < s.length; i++) {
        if (s[i] == previousChar) {
            result ++;
        }
        else {
            previousChar = s[i];
        }
    }
    
    return result;
}
