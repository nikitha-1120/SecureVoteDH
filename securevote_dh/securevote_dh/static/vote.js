function vote(candidate){

let voter=localStorage.getItem("voter")

fetch("/vote",{
method:"POST",
headers:{'Content-Type':'application/x-www-form-urlencoded'},
body:"voter="+voter+"&candidate="+candidate
})
.then(res=>res.json())
.then(data=>{

if(data.status==="already_voted"){

document.getElementById("msg").innerText="You already voted"

}
else if(data.status==="success"){

document.getElementById("msg").innerText="Vote submitted successfully"

localStorage.removeItem("voter")

setTimeout(()=>{
window.location="/login_page"
},2000)

}

})

}