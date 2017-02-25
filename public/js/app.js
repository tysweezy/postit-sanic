let posts = [];

axios.get('api/posts')
    .then(function(response) {
        for (var i = 0; i < response.data.length; i++) {
            console.log(posts);
            posts.push(response.data[i])
        }
    })
    .catch(function(err) {
        console.log(err);
    });


new Vue({
  el: "#app",
  data: {
      posts: posts,
      post: {
          title: '',
          body: ''
      }
  },
  
  methods: {
      newPost: function(e) {
          e.preventDefault();

          // don't submit from if fields are empty
          if (!this.post.title || !this.post.body) {
              return;
          }
          
          post_obj = {
              title: this.post.title,
              body: this.post.body
          }
 
          posts.push(post_obj);
          axios({
            method: 'POST',
            url: '/api/post/create',
            data: post_obj
          });

          // clear the form
          this.post.title = '';
          this.post.body = '';
      }
  }
});