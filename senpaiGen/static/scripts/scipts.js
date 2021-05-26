const post = document.getElementById('post');
const loadBtn = document.getElementById('load-more-button')


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
<hr>${el.author} | ${el.date_added}
<h6>${el.comment}</h6>
`});

if(response.size === 0){
        document.getElementById(`comment-endbox-${clickedPostId}`).innerHTML = "<hr>No Comment have been added yet<hr><br>"
        }
        else if (response.size < visibleComment){
        console.log(response.size, visibleComment)
        clickedBtn.classList.add('not-visible');
        document.getElementById(`comment-endbox-${clickedPostId}`).innerHTML = "<hr>No more comments...<hr><br>"
        }
        else{
        visibleComment +=4;
        clickedBtn.setAttribute('data-visibleComment', visibleComment);
        }
},
error: function(error){
console.log(error)
clickedBtn.innerHTML = "Try again Later !..."
}
})

}))
}



let visible = 3;


// The below code will perform the async Http(ajax) request

const getPost = () => {
$.ajax({
    type: "GET",
    url: `/data/${visible}/`,
    success: function(response){

    // response data because the key in dict is 'data'(which we've assigned in the views.py of posts
    const data = response.data;  // Assign the returned response to data constant

    // el is the short form of element

    data.forEach(el => {
        post.innerHTML += ` <h3>${el.title}</h3>
          <hr>
          ${el.body}
          <hr>
          ${el.image?

            `<div class='post-image'>
                <img src="${el.image}/" loading="lazy">
            </div>  <hr>`: ``}
            <div>
          ${el.author} | ${el.date}
          </div>
          <hr>

          <div class="btn-group" role="group" aria-label="Like comment Section">

          <div class='comments'>
           <button  class="btn btn-outline-secondary comment-button" id="comment-button-${el.id}" data-visibleComment="4" href="" data-postId="${el.id}">Load Comments | ${el.comment_count}</button>
            </div>

          <div id='like'>
              <form class="like-unlike-form" data-postId='${el.id}' type='submit'>
              <button class=${el.liked? `"btn btn-outline-danger"`: `"btn btn-outline-info"`} id='Like-button-${el.id}' data-href='${el.id}' href="">${el.liked ? `Unlike | ${el.like_count}`: `Like | ${el.like_count}` }</button>
              </form>
           </div>
           </div>
            <br>
            <div id="comments-${el.id}">
           </div>
           <div id="comment-endbox-${el.id}"
           </div>
           <hr>

          `
        })

        if(response.size === 0){
        document.getElementById('endBox').innerHTML = "No Post's have been added yet"
        }else if (response.size < visible){
        loadBtn.classList.add('not-visible');
        document.getElementById('endBox').innerHTML = "That's all..."
        }
        else{
        visible+= 3 }
        like_count_for_posts()  // call the like counter function
        commentLoader()  // To load comment on click
        },
    error: function(error){
        console.log(error)
    },
});

}

getPost()
loadBtn.addEventListener('click', () => {
getPost()
})

