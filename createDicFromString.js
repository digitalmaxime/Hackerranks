s = 'aabbccddeef'

let map = new Map();
for (let char of s) {
    map.set(char, map.get(char) + 1 || 1);
}

console.log(map)

// find min value of map values

let minNbOfOccurences = 1000000;
for (let key of map.keys()) {
    console.log("key : ", key, " value : ", map.get(key));
    if (map.get(key) < minNbOfOccurences) {
        minNbOfOccurences = map.get(key);
    }
}
console.log("map size : ", map.size)