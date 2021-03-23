<template>
  <div id="recommend" class="container">
    <button class="btn btn-dark" @click="getRecommendList()">영화추천받기</button>
      <div class="row justify-content-center">
      <h2>오늘의 추천작!</h2>
        <RecommendCarousel :recommendMovieList="recommendList" />
    </div>
  </div>
</template>

<script>
import RecommendCarousel from './RecommendCarousel.vue'
import axios from 'axios'

const API_URL = process.env.VUE_APP_SERVER_URL
const userId = localStorage.getItem('user_id')**1

export default {
  name: 'Recommend',
  components: {
    RecommendCarousel,
  },
  data: function () {
    return {
      recommendList: [],
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    getRecommendList: function () {
      const config = this.setToken()

      axios.get(`${API_URL}/movies/${userId}/recommend/`, config)
      .then((res) => {
        this.recommendList = res.data
        console.log(res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}

</script>

<style>
</style>