//variable delaration
let name="vianny"
let age ="20"
//function declaration
function add(a,b){
    return a+b
}    
//function call
result=add(9,7);
//range 
let fruits=["apple","banana", "mango","orange"];
let length=fruits.length;
for (let i =0;i<length; i++) {
    console.log(fruits[i]);
}
//output
console.log(name);
console.log(result)
let numstr=String(result);
// checking the type variable
console.log(typeof name); 
console.log(typeof result);
console.log(typeof numstr);
// concatenation
let gmail=(name +"@gmail.com");
console.log(gmail);
console.log(name+ "@" +age);