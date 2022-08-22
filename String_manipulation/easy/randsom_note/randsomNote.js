'use-strict'

function checkMagazine(magazine, note) {
    // Write your code here
    let magazineDic = new Map()
    for (let word of magazine) {
        magazineDic.set(word, magazineDic.get(word) + 1 | 0)
    }
    
    for (const word of note) {
        if (magazineDic.has(word) && magazineDic.get(word) > 0) {
            magazineDic[word] -= 1
        }
        else {
            console.log("No")
            return
        }
    }
    console.log("Yes")
}


magazineList = ['baby', 'powder', 'explosion', 'explosion', 'explosion']
noteList = ['baby', 'explosion']

checkMagazine(magazineList, noteList)