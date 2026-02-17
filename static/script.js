function showToast(msg){
    let t = document.getElementById("toast");
    t.innerText = msg;
    t.className = "show";
    setTimeout(()=> t.className = "", 3000);
}

function addCart(id){
fetch("/add", {
method:"POST",
headers: {"Content-Type":"application/json"},
body: JSON.stringify({id:id})
})
.then(r=>r.json())
.then(data=>{
    showToast(data.msg);
    updateCart(data.cart);
});
}

function buyNow(id){
fetch("/buy", {
method:"POST",
headers: {"Content-Type":"application/json"},
body: JSON.stringify({id:id})
})
.then(r=>r.json())
.then(data=>{
    showToast(data.msg);
});
}

function updateCart(cart){
    let list=document.getElementById("cart");
    let total=0;
    list.innerHTML="";

    cart.forEach(i=>{
        list.innerHTML += `<li>${i.name} - ₹${i.price}</li>`;
        total += i.price;
    });

    document.getElementById("total").innerText = "Total: ₹" + total;
}
