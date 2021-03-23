<template>
  <div>
    <div v-for="(movie, idx) in recommendMovieList" :key="idx">
      <div class="card-recommend">
        <div class="col-md-6 col-sm-12">
          <img :src="movie.poster_path" class="card-img-recommend " alt="">
        </div>
        <div class="card-body col-md-6 col-sm-12">
          <p class="card-title-recommend">{{ movie.title }}</p>
          <span v-for="(genre, idx) in movie.genre_ids" :key="idx">
            <span class="text-muted" >{{ genre.name }} </span>
          </span>
          <p class="text-muted" >WATCHUB! 좋아요: {{ movie.like_users.length }} </p>
          <p class="text-muted" >WATCHUB! 본 사람: {{ movie.watch_users.length }} </p>
          <span class="text-muted" >{{ movie.overview }} </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'RecommentCarousel',
  props: {
    recommendMovieList: Array,
  },
  components: {
  }
}
</script>

<style>
.card-recommend {
  display: flex;
  margin-bottom: 1rem;
  background-color: #000;
  flex-direction: row;
} 
.card-img-recommend {
  width: 100%;
  height: auto;
}
.card-title-recommend {
  color: #fff !important; 
  font-size: 2rem;
}
@media (max-width: 768px) {
  .card-recommend {
    display: flex;
    margin-bottom: 1rem;
    background-color: #000;
    flex-direction: column;
  } 
  .card-img-recommend {
    width: 100%;
    height: auto;
  }
  .card-title-recommend {
    color: #fff !important; 
    font-size: 1rem;
  }
}
</style>