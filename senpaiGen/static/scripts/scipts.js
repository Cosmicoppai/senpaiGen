
// Csrf Token Code Copied from Django Documentation

const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


// Ajax call to track like

const like_count_for_posts = () => {
const likeUnlikeForms = [...document.getElementsByClassName("like-unlike-form")]  // Class name defined in the html form(like-form)
likeUnlikeForms.forEach(form => form.addEventListener('submit', e => {
e.preventDefault();
const clickedId = e.target.getAttribute("data-postId")  // same as e.target.attribute("data-postId") and data-postId is the id(primary key) mentioned in the form
const clickedBtn = document.getElementById(`Like-button-${clickedId}`)

const btnMsg = clickedBtn.innerHTML // Read the text on the like button

if(btnMsg[0] == "L"){  // If the status is liked change it to Unliked and subtract 1 from the like count
const likeCount = parseInt(btnMsg[btnMsg.length - 1]) + 1;
clickedBtn.innerHTML = `Unlike | ${likeCount}`;
clickedBtn.className = "btn btn-outline-danger";
}
else{  // If status is Unliked change it to the Like and add 1 like
const likeCount = parseInt(btnMsg[btnMsg.length - 1]) - 1;
clickedBtn.innerHTML = `Like | ${likeCount}`;
clickedBtn.className = "btn btn-outline-info";
}

$.ajax({
type: 'POST',
url: `/post/like/`,
data: {
'csrfmiddlewaretoken': csrftoken,
'pk': clickedId,
},
error: function(error){
console.log(error)
clickedBtn.innerHTML += '<hr> Unable to process request! Try again Later'
}
})
}))
}

// Comment Loader Function

const commentLoader = () => {
const commentDiv = [...document.getElementsByClassName('comment-button')]
commentDiv.forEach(div => div.addEventListener('click', e => {
e.preventDefault();
const clickedPostId = e.target.getAttribute('data-postId');  //el.id
const clickedBtn = document.getElementById(`comment-button-${clickedPostId}`)  // Id of the clicked button
let visibleComment = parseInt(clickedBtn.getAttribute('data-visibleComment'));  // get the visibleComment attribute(i.e no of comments which we've to load)

$.ajax({
type: 'GET',
url: `/comment/${clickedPostId}/${visibleComment}`,

success: function(response){
const data = response.data
const comments = document.getElementById(`comments-${clickedPostId}`)  // get the div in which comments are going to load

data.forEach(el => {
comments.innerHTML += `
<hr>
<div class="card">
<div class="card-body">
<div class="blockquote"><p class="card-text">${el.comment}</div>
<div class="blockquote-footer text-end"><a href="/profile/${el.author}">${el.author}</a> | ${el.date_added}</div>
</div>
</div>
`});

if(response.size === 0){
        document.getElementById(`comment-endbox-${clickedPostId}`).innerHTML = "<hr>No Comment have been added yet<hr><br>"
        }
        else if (response.size < visibleComment){
        clickedBtn.classList.add('not-visible');
        document.getElementById(`comment-endbox-${clickedPostId}`).innerHTML = "<hr>No more comments...<hr><br>"
        }
        else{
        visibleComment +=4;
        clickedBtn.setAttribute('data-visibleComment', visibleComment);
        }
},
error: function(error){
clickedBtn.innerHTML = "Try again Later !..."
}
})

}))
}


// function to add comment

const addComment = () => {
const commentForms = [...document.getElementsByClassName("comment-form")]  // Class name defined in the html form(like-form)
commentForms.forEach(form => form.addEventListener('submit', e => {
e.preventDefault();

const newCommentPostId = e.target.getAttribute("data-postId")  // same as e.target.attribute("data-postId") and data-postId is the id(primary key) mentioned in the form
const newCommentText = document.getElementById(`comment-area-${newCommentPostId}`)


$.ajax({
type: 'POST',
url: '/post/comment/',
data: {'csrfmiddlewaretoken':csrftoken,
    'comment':newCommentText.value,
    'pk':newCommentPostId,
},
datatype:"json",

success: function(response){
form.reset()
document.getElementById(`comment-endbox-${newCommentPostId}`).innerHTML= `<hr> ${response.data.msg}`;
},

error: function(error){
document.getElementById(`comment-endbox-${newCommentPostId}`).innerHTML= '<hr> Unable to process request! Try again Later'
}
})
}))
}




