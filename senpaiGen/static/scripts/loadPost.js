const post = document.getElementById('post');
const loadBtn = document.getElementById('load-more-button')

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
        post.innerHTML += ` <div class="col d-flex justify-content-center">
        <div class="card w-50 border-secondary mb-3">
        <h3 class="card-title">${el.title}</h3>
          <hr>
          <div class="card-body blockquote" id="post-body">
          ${el.body}
          <hr>
          ${el.image?

            `<div class='post-image'>
                <img src="${el.image}/" loading="lazy" class="img-fluid">
            </div> <hr>`: ``}
            <p class="blockquote-footer text-end">
                ${el.author} | ${el.date}
          <hr>
          </div>
          <div class="card-body">

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
           </div>
           <hr>
           </div>

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

