"use strict";

function test(input) {
    input = input.split("\n");
    // console.log(input)
    let start_end_time = input[0].split(" ");
    for (let i = 0; i < start_end_time.length; i++) {
        start_end_time[i] = parseInt(start_end_time[i]);
    }

    // console.log(start_end_time);

    let map_adjacence = new Map();
    let map_proba = new Map();
    for (let i = 1; i < input.length; i++ ) {
        let entry = input[i].split(" ");
        for (let j = 0; j < entry.length; j++) {
            if (j == 1) {
                entry[j] = parseFloat(entry[j])
            } else {
                entry[j] = parseInt(entry[j])
            }
        }

        let neighbours = []
        for (let j = 2; j < entry.length - 1; j+=2) {
            let tuple = [entry[j], entry[j+1]];
            neighbours.push(tuple);
        }
        // console.log(neighbours);
        map_adjacence.set(entry[0], neighbours);
        map_proba.set(entry[0], entry[1]);
    }
    // console.log(map_adjacence)

    const possible_paths = [];
    let queue = [];
    queue.push([start_end_time[0]]);
    while (queue.length != 0) {
        let top = queue.pop();
        const lastElement = top[top.length-1];
        if (lastElement == start_end_time[1]) {
            possible_paths.push([...top])
        }
        else {
            let top_neighbours = map_adjacence.get(lastElement);
            top_neighbours = top_neighbours.filter(ele => !top.includes(ele[0]))
    
            if (top_neighbours.length > 0) {
                for (const neighbour_dist of top_neighbours) {
                    const newEntrieInQueue = [...top]
                    newEntrieInQueue.push(neighbour_dist[0]);
                    queue.push(newEntrieInQueue);
                }
            }
        }  
    }
    // console.log("Queue : ", queue)
    // console.log("Possible paths  : ", possible_paths)
    
    // filter out path that are too long
    const filteredPossiblePath = possible_paths.filter(path => {
        let tempTotalTime = 0;
        for (const [idx,id] of path.entries()) {
            if (idx < path.length - 1) {
                let id_neighbours = map_adjacence.get(id)
                const next_path_stop = path[idx + 1];
                let id_time = id_neighbours.filter(ele => ele[0] == next_path_stop)[0]
                // console.log(id_time)
                tempTotalTime += id_time[1];
            }
        }
        if (tempTotalTime <= start_end_time[2]) {
            return true;
        }
    })

    // validate if there is a possible path
    if (filteredPossiblePath.length == 0) {
        //...
    }

    // keep only the one w lowest proba of death
    let lowestProbaOfDying = 100;
    let bestPath = filteredPossiblePath[0];
    for (let path of filteredPossiblePath) {
        let tempCurrentProbaOfDying = 0;
        path.forEach(id => {
            tempCurrentProbaOfDying += map_proba.get(id);
        })
        if (tempCurrentProbaOfDying < lowestProbaOfDying) {
            lowestProbaOfDying = tempCurrentProbaOfDying;
            bestPath = path;
        }
    }

    // console.log(filteredPossiblePath);
    // console.log(bestPath);
    const res = bestPath.join(" ");
    console.log(res);

}


let input = "0 4 20\n0 0.1 1 1 2 10 3 1\n1 0.5 0 1 4 1\n2 0.0 0 10 4 11\n3 0.1 0 1 4 1\n4 0.3 1 1 2 11 3 1";

test(input)