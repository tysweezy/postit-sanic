let posts = [];

axios.get('api/posts')
    .then(function(response) {
        for (var i = 0; i < response.data.length; i++) {
            posts.push(response.data[i])
        }
    })
    .catch(function(err) {
        console.log(err);
    });



var app = new Vue({
  el: "#app",
  data: {
      posts: posts
  },
  
  methods: {
      newPost: function() {
          // create new post
      }
  }
});