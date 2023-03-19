function totalBudget(){
    let rows = document.getElementsByName("rows");
    let projected = 0;
    let actual = 0;
    for(let i =0; i < rows.length; i++){
        projected = projected + parseInt(rows[i].children[2].innerText);
        actual = actual + parseInt(rows[i].children[3].innerText);
    }
    return (projected-actual);
}
let total = document.getElementById("total");
if(totalBudget() >= 0){
    total.style = "color: green; size: 24vh;";
    total.innerText = "There is a projected budget surplus of $ " + totalBudget();
}
else{
    total.style = "color: red; size: 24vh;";
    total.innerText = "There is a projected budget deficit of $ " + totalBudget();
}
