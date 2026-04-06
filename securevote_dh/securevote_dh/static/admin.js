fetch("/results")
.then(res=>res.json())
.then(data=>{

let votes={}

data.forEach(row=>{
votes[row[0]]=row[1]
})

let candidates=["Candidate A","Candidate B","Candidate C"]

let total=0

let table=document.getElementById("voteTable")

candidates.forEach(c=>{

let v=votes[c]||0

total+=v

let row=document.createElement("tr")

row.innerHTML="<td>"+c+"</td><td>"+v+"</td>"

table.appendChild(row)

})

document.getElementById("totalVotes").innerText=total

})