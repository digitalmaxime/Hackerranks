arr = [7, 7, 7, 7]

let nbPeak = 0;
// for (const[index, ele] of arr.entries()) {
for (let i = 0; i < arr.length; i++) {
    if (i != 0 && i != arr.length - 1) {
        let current = arr[i];
        let previous = arr[i - 1]
        let next = arr[i + 1]
        if (arr[i] > arr[i - 1] && arr[i] > arr[i + 1]) {
            nbPeak++;
        }
    }
}
console.log(nbPeak);