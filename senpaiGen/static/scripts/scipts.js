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

$.ajax({
type: 'POST',
url: `/post/like/`,
data: {
'csrfmiddlewaretoken': csrftoken,
'pk': clickedId,
},
success: function(response){
clickedBtn.innerHTML = `${response.msg} | ${response.total_no_of_likes}`
if(response.msg == 'Like'){
clickedBtn.style.color = 'blue';
}else{
clickedBtn.style.color = 'red';
}
},

error: function(error){
console.log(error)
clickedBtn.innerHTML += '<hr> Unable to process request! Try again Later'
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
            <div class='post-image'>
                <img src="${el.image}/" loading="lazy">
            </div>
          <hr>
            <div>
          ${el.author} | ${el.date}
          </div>
          <hr>
          <div id='comments'>
          <a href='post/comment/${el.id}/'>comments | ${el.comment_count}</a>
          </div>

          <div id='like'>
          <form class="like-unlike-form" data-postId='${el.id}' type='submit'>
          <button id='Like-button-${el.id}' data-href='${el.id}' href="#">${el.liked ? `Unlike | ${el.like_count}`: `Like | ${el.like_count}` }</button>
          </form>
          </div>

          `

        // `$(el.liked ? 'Unlike' : 'Like')`
        if(el.liked === true){
        document.getElementById(`Like-button-${el.id}`).style.color = 'red';
        // like_obj.innerHTML = 'Unlike'
        }else{
        document.getElementById(`Like-button-${el.id}`).style.color = 'blue'
        }
        })

        if(response.size === 0){
        document.getElementById('endBox').innerHTML = "No Post's have been added yet"
        }else if (response.size <= visible){
        loadBtn.classList.add('not-visible');
        document.getElementById('endBox').innerHTML = "That's all..."
        }
        else{
        visible+= 3 }
        like_count_for_posts()  // call the like counter function
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

