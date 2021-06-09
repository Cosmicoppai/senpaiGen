var addPostButton = document.getElementById('add-new-post')
var postAddForm = document.getElementById('post-add-form')


$(postAddForm).submit(function(e){
e.preventDefault();

var formData = new FormData(this);
$.ajax({
type: "POST",
url: "/new_post",
data: formData,

success: function(response){
postAddForm.reset();  // document.getElementById(#formId).reset()  -> It'll reset the form
alert('Post has been Successfully posted');

},
error: function(response){

},
cache: false,
contentType: false,
processData: false
})
})