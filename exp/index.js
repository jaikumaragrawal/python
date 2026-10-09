let button=document.querySelector("#submit");
let input=document.querySelector("#todo");
let container=document.querySelector("#showtodo")
let todod=[];

button.addEventListener('click',function(){
    let value =input.value;
    // console.log(value)
    let obj={
        title:input.value,
        status:false
    };
    todod=[...todod,obj];
    showTodo(todod);
});

 
function showTodo(todod){
    container.innnerhtml=null;
    todod.forEach((item) =>{
        let h2=document.createElement("h2");
        let div=document.createElement("div");
        h2.textContent=item.title;
        
        
        container.append(h2)

    });
};