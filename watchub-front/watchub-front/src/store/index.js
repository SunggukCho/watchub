import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    LatestList: [],
    PopularList: [],
    ClassicList: [],
    wishList: [],
    alreadyList: [],
    favoriteList: [],
    userId: 0,
    flag: true,
  },
  mutations: {
    SET_LATEST_MOVIE_LIST: function (state, movies) {
      state.LatestList = movies
    },
    SET_POPULAR_MOVIE_LIST: function (state, movies) {
      state.PopularList = movies
    },
    SET_CLASSIC_MOVIE_LIST: function (state, movies) {
      state.ClassicList = movies
    },
    SET_WISH_LIST: function (state, wish) {
      state.wishList.push(wish)
    },
    SET_WATCHED_MOVIE_LIST: function (state, movie) {
      state.alreadyList.push(movie)
    },
    RESET_WATCHED_MOVIE_LIST: function (state, movie) {
      const index = state.alreadyList.indexOf(movie)
      state.alreadyList.splice(index, movie)
    },
    SET_USER_ID: function (state, userId) {
      state.userId = userId
    },
    SET_LIKE_MOVIE_LIST: function (state, movie) {
      state.favoriteList.push(movie)
    },
    RESET_LIKE_MOVIE_LIST: function (state, movie) {
      const index = state.favoriteList.indexOf(movie)
      state.favoriteList.splice(index, movie)
    },
  },
  actions: {
    getLatestMovieList: function({commit}, movies) {
      commit('SET_LATEST_MOVIE_LIST', movies)
    },
    getPopularMovieList: function({commit}, movies) {
      commit('SET_POPULAR_MOVIE_LIST', movies)
    },
    getClassicMovieList: function({commit}, movies) {
      commit('SET_CLASSIC_MOVIE_LIST', movies)
    },
    getWishList: function({commit}, wish) {
      commit('SET_WISH_LIST', wish)
    },
    getWatchedmovie: function ({commit}, movie) {
      commit('SET_WATCHED_MOVIE_LIST', movie)
    },
    removeWatchedmovie: function ({commit}, movie) {
      commit('RESET_WATCHED_MOVIE_LIST', movie)
    },
    getLikeMovie: function ({commit}, movie) {
      commit('SET_LIKE_MOVIE_LIST', movie)
    },
    removeLikeMovie: function ({commit}, movie) {
      commit('RESET_LIKE_MOVIE_LIST', movie)
    },
  },
  modules: {
  },
  plugins: [
    createPersistedState(),
  ]
})
