function processData(input) {
    //Enter your code here
    input = input.split("\n")
    // console.log(input)
    nb_of_tests = parseInt(input[0])
    // console.log("nb of tests : ", nb_of_tests)
    for (let i = 0; i < nb_of_tests; i++) {
        N_B = input[1 + i * 2].split(" ")
        N = N_B[0];
        B = N_B[1];
        
        Ai = input[2 + i * 2].split(" ")
        for (let j = 0; j < Ai.length; j++) {
            Ai[j] = parseInt(Ai[j]);
        }
        
        Ai.sort((a, b) => a - b)
        // console.log('N : ', N, ", B : ", B, ", Ai : ", Ai);
        
        total_nb_food_item = 0;
        index = 0;
        while (B > 0) {
            if (B >= Ai[index]) {
                total_nb_food_item++;
                B -= Ai[index];
            }
            else {
                break;
            }
            
            index ++;
        }
        
        if (total_nb_food_item == 0) {
            total_nb_food_item = '0 "*va voler des pogos au CEG*"'
        }
        console.log("Case #" + (i+1) + ": " + total_nb_food_item)
    }
} 