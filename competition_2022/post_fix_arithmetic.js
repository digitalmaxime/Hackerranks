class Operator {
    constructor(symbol) {
        this.symbol = symbol;
        this.priority = this.definePriority(this.symbol);
    }
    
    definePriority = () => {
        if (["+", "-"].includes(this.symbol)) {
            return 0;
        }
        else if (["*", "/"].includes(this.symbol)) {
            return 1;
        }
        else if (['(', ')'].includes(this.symbol)) {
            return  -1;
        }
        else if (['sin', 'cos', 'tan'].includes(this.symbol)) {
            return  3;
        }
        else if (['^'].includes(this.symbol)) {
            return  2;
        }
    }
    
    greaterThan = (operator) => {
        return this.priority > operator.priority;
    }
}

// s = "12+(3*2)";
input = "5+(2+3^4)";
stack = [];
string_builder = "";

plus_minus = ["+", "-"];
mult_div = ["*", "/"];
parenthesis = ['(', ')'];
functions = ['sin', 'cos', 'tan'];
exponent = ['^'];
operators = plus_minus.concat(mult_div).concat(functions).concat(exponent);
equation_array = input.split("")
for (const [index, char] of equation_array.entries()) {
    let look_ahead2 = equation_array.slice(index, index+3).join("")
    if (char >= '0' && char <= '9') {
        string_builder += char;
    }

    else if (operators.includes(char)) {
        if (string_builder[string_builder.length - 1] != " ") {
            string_builder += " ";
        }

        let operator = new Operator(char);

        if (stack.length == 0) {
            stack.push(operator);
        }
        else if (operator.greaterThan(stack[stack.length - 1])) { // more precedence
            stack.push(operator);
        }
        else {
            top_stack = stack.pop();
            string_builder += top_stack.symbol;
            if (string_builder[string_builder.length - 1] != " ") {
                string_builder += " ";
            }
            stack.push(operator);
        }

    }

    else if (operators.includes(look_ahead2)) {
        if (string_builder[string_builder.length - 1] != " ") {
            string_builder += " ";
        }        
        
        let operator = new Operator(look_ahead2);

        if (stack.length == 0) {
            stack.push(operator);
        }
        else if (operator.greaterThan(stack[stack.length - 1])) { // more precedence
            stack.push(operator);
        }
        else {
            top_stack = stack.pop();
            string_builder += top_stack.symbol;
            if (string_builder[string_builder.length - 1] != " ") {
                string_builder += " ";
            }
            stack.push(operator);
        }

    }

    else if (char == "(") {
        let operator = new Operator(char);
        stack.push(operator);
    }

    else if (char == ")") {
        if (string_builder[string_builder.length - 1] != " ") {
            string_builder += " ";
        }     
        top_stack = stack.pop();
        while (top_stack.symbol != "(") {
            string_builder += top_stack.symbol;
            if (string_builder[string_builder.length - 1] != " ") {
                string_builder += " ";
            }            
            top_stack = stack.pop();
        }
    }
}
if (string_builder[string_builder.length - 1] != " ") {
    string_builder += " ";
}     
while (stack.length > 0) {
    top_stack = stack.pop();
    string_builder += top_stack.symbol;
    if (string_builder[string_builder.length - 1] != " ") {
        string_builder += " ";
    }     
}



// op1 = new Operator('+')
// console.log(op1)
// op2 = new Operator('-')
// console.log(op2)
// op3 = new Operator('*')
// console.log(op3)
// op4 = new Operator('(')
// console.log(op4)

// console.log("is + greater than - ? : ", op1.greaterThan(op2))
// console.log("is * greater than + ? : ", op3.greaterThan(op1))
// console.log("is ( greater than - ? : ", op4.greaterThan(op2))
// console.log("is ( greater than * ? : ", op4.greaterThan(op3))
// console.log("is * greater than ) ? : ", op3.greaterThan(op4))
console.log(string_builder)

