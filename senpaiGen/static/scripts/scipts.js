/*function() change{
  document.getElementById("1").innerHTML = "Yes it's working!.."
}


$("#2").bind("click", change);*/

document.getElementById('id2').onclick = function(){
  document.getElementById("id1").innerHTML = "機能しています !.."
  var boi = document.getElementById("body")
  boi.style.position = "fixed";
  boi.style.padding = 0;
  boi.style.margin = 0;
  boi.style.top = 0;
  boi.style.left = 0;
  boi.style.width = "100%";
  boi.style.height = "100%";
  boi.style.background = "linear-gradient(black, #000099, #66c2ff, #ffcccc, #ffeee6)"

}

document.getElementById('like').onclick = () => {
let obj = document.getElementById('like');
if(obj.innerHTML == 'Like'){
obj.innerHTML = 'Unlike'
obj.style.color = 'red'
}else{
obj.innerHTML = 'Like'
obj.style.color = 'blue'
}
}
