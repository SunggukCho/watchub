<template>
  <div class="home">
    <Latest  />
    <Popular  />
    <Classic  />

  </div>
</template>

<script>
// @ is an alias to /src
import Latest from '@/components/Home/Carousel.vue'
import Popular from '@/components/Home/Popular.vue'
import Classic from '@/components/Home/Classic.vue'
import axios from 'axios'

const API_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Home',
  components: {
    Latest,
    Popular,
    Classic,
  },
  data: function () {
    return {
      movies: [
      ],
    }
  },
  computed: {
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
    getLatestMovies: function () {
      const config = this.setToken() 
      axios.get(`${API_URL}/movies/latest/`, config)
      .then((res) => {
        this.$store.dispatch('getLatestMovieList', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getPopularMovies: function () {
      const config = this.setToken() 
      axios.get(`${API_URL}/movies/popular/`, config)
      .then((res) => {
        this.$store.dispatch('getPopularMovieList', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getClassicMovies: function () {
      const config = this.setToken() 
      axios.get(`${API_URL}/movies/classic/`, config)
      .then((res) => {
        this.$store.dispatch('getClassicMovieList', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
  created: function () {
    this.getLatestMovies()
    this.getPopularMovies()
    this.getClassicMovies()
  }
}
</script>
