'use strict';

function sherlockAndAnagrams(s) {
    // Write your code here
    var result = 0;
    for (var i = 0; i < s.length; i++) {
        for (var j = i + 1; j < s.length; j++) {
            var dic1 = {};
            var dic2 = {};
            for (var k = 0; k < (j - i); k++) {
                if (s[i + k] in dic1) {
                    dic1[s[i + k]] += 1;
                }
                else {
                    dic1[s[i + k]] = 1;
                }

                if (s[j - k] in dic2)
                    dic2[s[j - k]] += 1;
                else
                    dic2[s[j - k]] = 1;

                console.log(dic1, dic2)
                let isEqual = true;
                for (let key in dic1){
                    if (dic1[key] != dic2[key]){
                        isEqual = false;
                    }
                }
                
                if (isEqual) result += 1;
            }
        }
    }
    return result;
}

const answer = sherlockAndAnagrams('abcba')
console.log(answer)
//# sourceMappingURL=anagrams_substring.js.map