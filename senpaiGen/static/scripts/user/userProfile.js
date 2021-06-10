const postRow = document.getElementById('post-row')
const author = document.getElementById('nickname').innerHTML  // Read the nickname from the profile name to retrieve that user's post only

let visible = 4

const loadPost = () => {
$.ajax({
type: 'GET',
url: `/post_list/${visible}/${author}`,
success: function(response){
const data = response.data;

data.forEach(el => {
postRow.innerHTML += `
 <div class="col-lg-6 mb-2 pr-lg-1"><img src="${el.image}" alt="" class="img-fluid rounded shadow-sm"></div>
`
})
visible+= 4;
},

error: function(response){
postRow.innerHTML += `<h3>Try again later </h3>`

}
})
};

loadPost();