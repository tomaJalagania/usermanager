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