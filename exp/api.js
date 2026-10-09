fetch("https://jsonplaceholder.typicode.com/users")
.then((res) => res.json())
.then((res) => showdata(res))
.catch((error) => console.log(error));


function showdata(users){

    const container = document.querySelector("#users");

    for(let i = 0; i < users.length; i++){

        container.innerHTML +=
        "<h2>" + users[i].name + "</h2>" +
        "<p>" + users[i].email + "</p>";

    }
}