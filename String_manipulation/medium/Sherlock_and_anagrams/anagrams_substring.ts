
function sherlockAndAnagrams(s: string): number {
    // Write your code here
    let result = 0
    
    for (let i = 0; i < s.length; i++) {
        for ( let j = i + 1; j < s.length; j++) {
            let dic1: {[key: string]: number} = {}
            let dic2: {[key: string]: number} = {}
            
            for (let k = 0; k < (j - i); k++) {
                if (s[i+k] in dic1) {
                    dic1[s[i+k]] += 1
                }
                else {
                    dic1[s[i+k]] = 1
                }
                    
                if (s[j-k] in dic2) dic2[s[j-k]] += 1
                else dic2[s[j-k]] = 1
                    
                if (dic1 == dic2) result += 1
            }
        }
    }
                        
    return result
}

console.log('hello world')