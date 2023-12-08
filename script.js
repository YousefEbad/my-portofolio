
const menu = document.getElementById("menu");
const action = document.getElementById("action");
const ho = document.getElementById("ho");
const ab = document.getElementById("ab");
const se = document.getElementById("se");
const sk = document.getElementById("sk");
const co = document.getElementById("co");

menu.addEventListener("click", ()=>{
    handleMenu();
})

ho.addEventListener("click", ()=>{
    handleMenu();
})
ab.addEventListener("click", ()=>{
    handleMenu();
})
se.addEventListener("click", ()=>{
    handleMenu();
})
sk.addEventListener("click", ()=>{
    handleMenu();
})
co.addEventListener("click", ()=>{
    handleMenu();
})


function handleMenu(){
    menu.classList.toggle("is-active");
    action.classList.toggle("is-active");
    ho.classList.toggle("is-active");
}



