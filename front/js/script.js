window.addEventListener("load",async e=>{
    let res = await fetch("http://localhost:5000/users")
    if(!res.ok) {
        throw new Error(res.statusText)
    }
    obj = JSON.parse(JSON.stringify(await res.json()))
    
    let tbody = document.getElementById("tbd")
    obj.forEach(user=>{
        let tr = document.createElement("tr")
        let tdn = document.createElement("td")
        let tde = document.createElement("td")
        let tdid = document.createElement("td")
        tdn.textContent = user.Username
        tde.textContent = user.Email
        tdid.innerHTML = `<button data-id=${user.id} onclick="deleteuser(this)">Delete</button>`
        tr.appendChild(tdn)
        tr.appendChild(tde)
        tr.appendChild(tdid)
        tbody.appendChild(tr)
    })

   
}) 
let btn = document.getElementById("btn")

btn.addEventListener("click", async e=>{
        e.preventDefault()
        let uname = document.getElementById("name")
        let email = document.getElementById("email")
        if(email.value == ""|| uname.value=="") {
            window.alert("inputs are empty")
            return
        }
        let res = await fetch("http://localhost:5000/add",{
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({"Username":uname.value,"Email":email.value})
        })
        obj = await res.json()
        
        obj.error? window.alert(obj.error):""
})

async function deleteuser(e) {
    let btn = e
        
        let res = await fetch("http://localhost:5000/del",{
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({"id": btn.dataset["id"]})
        })
        obj = await res.json()
        window.alert(obj.msg)
        //obj.error? window.alert(obj.error):""
}