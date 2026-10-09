fetch("https://dummyjson.com/products?limit=0")
    .then((res) => res.json())
    .then((res) => showproduct(res.products))
    .catch((error) => console.log(error));


// function showdata(products){

//     const container = document.querySelector("#products");

//     for(let i = 0; i < users.length; i++){

//         container.innerHTML +=
//         "<h2>" + users[i].title + "</h2>" +
//         "<p>" + users[i].description + "</p>"+
//          "<p>" + users[i]. + "</p>"


//     }

 



function showproduct(products) {
    const container = document.querySelector("#products");
    container.innerHTML = null;

    products.forEach((item) => {
        let h2 = document.createElement("h2");
         h2.textContent = item.title;
        container.append(h2);
        let div = document.createElement("div");
        div.textContent = item.description;
        container.append(div);
        let p2=document.createElement("img");
        p2.src=item.images
        container.append(p2)
        
        
    });
}