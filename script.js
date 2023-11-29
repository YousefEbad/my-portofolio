
const menu = document.getElementById("menu");
const action = document.getElementById("action");

menu.addEventListener("click", ()=>{
    handleMenu();
})
function handleMenu(){
    menu.classList.toggle("is-active");
    action.classList.toggle("is-active");
}



