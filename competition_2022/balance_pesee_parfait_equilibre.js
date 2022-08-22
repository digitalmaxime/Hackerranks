"use strict";

function func() {
    let fleau_gauche = [0, 3, 11, 14, 23];
    let fleau_droit = [0, 2, 5, 15, 24];
    // let fleau_gauche = [0, 13, 17, 3]
    // let fleau_droit = [0, 6, 6, 12, 21]
    fleau_droit = fleau_droit.filter(ele => ele != 0);
    fleau_gauche = fleau_gauche.filter(ele => ele != 0);
    fleau_droit.sort((a,b) => a-b);
    fleau_gauche.sort((a,b) => a-b);
    let total_min = 100000;
    let res = [];

    // for (let i = 0; i < fleau_gauche.length; i++) {
    //     for (let j = 0; j < fleau_droit.length; j++) {
    //         const nb_gauche_retenus = []
    //         const nb_droit_retenus = []
    //         let sum_left = 0;
    //         let sum_right = 0;
    //         let left_it = i;
    //         let right_it = j;

    //         while (left_it < fleau_gauche.length || right_it < fleau_droit.length) {
    //             if (sum_left > sum_right && right_it < fleau_droit.length) {
    //                 sum_right += fleau_droit[right_it];
    //                 nb_droit_retenus.push(fleau_droit[right_it])
    //                 right_it ++;
    //             } else  if (left_it < fleau_gauche.length) {
    //                 sum_left += fleau_gauche[left_it];
    //                 nb_gauche_retenus.push(fleau_gauche[left_it])
    //                 left_it ++;
    //             } else {
    //                 break;
    //             }

    //             if (sum_left == sum_right) {
    //                 if (sum_left < total_min) {
    //                     total_min = sum_left
    //                     res = nb_gauche_retenus.concat(nb_droit_retenus)
    //                     res = res.join(",")
    //                 }
    //             }
    //         }
    //     }
    // }

    for (let i = 0; i < fleau_droit.length; i++) {
        for (let j = 0; j < fleau_gauche.length; j++) {
            let sum_left = 0;
            let sum_right = 0;
            const nb_gauche_retenus = []
            const nb_droit_retenus = []
            let right_it = i;
            let left_it = j;

            while (left_it < fleau_gauche.length || right_it < fleau_droit.length) {
                if (sum_left > sum_right && right_it < fleau_droit.length) {
                    sum_right += fleau_droit[right_it];
                    nb_droit_retenus.push(fleau_droit[right_it])
                    right_it ++;
                } else if (left_it < fleau_gauche.length) {
                    sum_left += fleau_gauche[left_it];
                    nb_gauche_retenus.push(fleau_gauche[left_it])
                    left_it ++;
                } else {
                    break;
                }
                if (sum_left == sum_right) {
                    if (sum_left < total_min) {
                        total_min = sum_left
                        res = nb_gauche_retenus.concat(nb_droit_retenus)
                        res = res.join(",")
                    }
                }
            }
        }
    }

    if (res.length == 0) {
        console.log(0)
    } else {
        console.log(res)
    }
}


func();