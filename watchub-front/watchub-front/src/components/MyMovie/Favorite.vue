<template>
  <div id="favorite">
    <div class="nav">
      <router-link :to="{name: 'Favorite'}" class="innerLink"> 좋아하는 영화</router-link> |
      <router-link :to="{name: 'Already'}" class="innerLink"> 본 영화</router-link> |
      <router-link :to="{name: 'WishList'}" class="innerLink"> 나중에 볼 영화</router-link> 
    </div>
    <h2>내가 좋아하는 영화</h2>
    <div class="container">
      <div class="row">
        <div class="hello row row-cols-1 row-cols-md-3">
          <div class="col-md-4" v-for="(movie, idx) in favorite" :key="idx">
            <div class="card">
              <img :src="movie.poster_path" class="card-img-top" alt="">
                <div class="card-body">
                  <p class="card-title">{{ movie.title }}</p>
                  <span v-for="(genre, idx) in movie.genre_ids" :key="idx">
                    <span class="text-muted" >{{ genre.name }} </span>
                  </span>
                </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Favorite',
  data: function () {
    return {
      favorite: this.$store.state.favoriteList,
    }
  },
  methods: {

  },
}
</script>

<style>
.nav {
  display: block;
  padding: 30px;
}
.nav a {
  font-weight: bold;
  color: #d2d7db;
}
.nav a.router-link-exact-active {
  color: #42b983;
}
#favorite{
  text-align: center;
}
.innerLink {
  color: #fff;
  font-size: 1rem;
}
</style>