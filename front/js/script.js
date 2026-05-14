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
        tdn.textContent = user.Username
        tde.textContent = user.Email
        tr.appendChild(tdn)
        tr.appendChild(tde)
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