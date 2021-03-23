<template>
  <div id="myMovie">
    <div class="nav">
      <router-link :to="{name: 'Favorite'}" class="innerLink"> 좋아하는 영화</router-link> |
      <router-link :to="{name: 'Already'}" class="innerLink"> 본 영화</router-link> |
      <router-link :to="{name: 'WishList'}" class="innerLink"> 나중에 볼 영화</router-link> 
    </div>
  </div>
</template>

<script>
// import Favorite from '@/components/MyMovie/Favorite.vue'


export default {
  name: 'MyMovie',
  components: {
    // Favorite,
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
#myMovie{
  text-align: center;
}
.innerLink {
  color: #fff;
  text-decoration: none;
  font-size: 1rem;
}
</style>