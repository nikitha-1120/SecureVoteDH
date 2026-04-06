function login(){

let voter=document.getElementById("voterId").value

fetch("/login",{
method:"POST",
headers:{'Content-Type':'application/x-www-form-urlencoded'},
body:"voter="+voter
})
.then(res=>res.json())
.then(data=>{

if(data.status==="ok"){

localStorage.setItem("voter",voter)

window.location="/dh_page"

}
else{

alert("Invalid voter")

}

})

}