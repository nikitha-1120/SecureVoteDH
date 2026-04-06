function modExp(base,exp,mod){

let result=1

for(let i=0;i<exp;i++){
result=(result*base)%mod
}

return result

}

function runDH(){

let p=23
let g=5

let a=6
let b=15

let A=modExp(g,a,p)
let B=modExp(g,b,p)

let secret=modExp(B,a,p)

document.getElementById("A").innerText=A
document.getElementById("B").innerText=B
document.getElementById("secret").innerText=secret

}