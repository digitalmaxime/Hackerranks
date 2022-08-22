# // Dividende = 18;
# // Divisor = 19;

# // let exp_divisor = Math.log(Divisor) / Math.log(2);
# // let exp_divisor_ceil = Math.ceil(exp_divisor)
# // let base_divisor = Divisor / 2 ** exp_divisor_ceil;
# // let F_factor = base_divisor / Divisor;    
# // let base_dividende = Dividende * F_factor;
# // // console.log("exp_divisor = ", exp_divisor)
# // console.log("base_dividende : ", base_dividende)
# // // console.log("Dividende : ", Dividende)
# // console.log("base_divisor : ", base_divisor)
# // console.log("*********")
# // for (let i = 0; i < 5; i++) {
# //     Divisor *= base_divisor;
# //     x = (1 / base_divisor) / 2
# //     // Dividende *= base_dividende;
# //     // exp_divisor = Math.log(Divisor) / Math.log(2);
# //     // exp_divisor_ceil = Math.ceil(exp_divisor)
# //     // base_divisor = Divisor / 2 ** exp_divisor_ceil;
# //     // F_factor = base_divisor / Divisor;    
# //     // Dividende *= F_factor;
# //     // console.log("Dividende : ", Dividende)
# //     // console.log("base_divisor : ", base_divisor)
# //     // console.log("*********")
# // }


# // : Initialize: 
N = 18
D = 19
F = 1 - 0.1 / 19

for i in range(5):
    N = N * F
    D = D * F
    F = (2 - D)
    # N = (1 - ni) * N * F_minus_one
    # D = (1 + di) * D * F_minus_one
    # F = (1 - fi) * (2 - D)
