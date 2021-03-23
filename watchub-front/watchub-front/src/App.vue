<template>
  <div id="app" class="container-fluid">
    <div id="nav">
      <a v-if="login === true" href="/"><img alt="Watchub logo" src="./assets/logo_watchub.png" class="main_logo"></a>
      <a v-else><img alt="Watchub logo" src="./assets/logo_watchub.png" class="main_logo"></a>
      <span v-if="login">
        <router-link to="/">Home</router-link> |
        <router-link to="/recommend">추천영화</router-link> |
        <router-link :to="{name: 'Favorite'}">MyMovie</router-link> |
        <router-link  @click.native="logout" to="#" >Logout</router-link>
      </span>
      <span v-else>
        <router-link :to="{ name: 'Signup' }">Signup</router-link> |
        <router-link :to="{ name: 'Login' }">Login</router-link> 
      </span>
    </div>
    <router-view @login="login=true" />
  </div>
</template>
<script>
export default {
  name: 'App',
    data: function () {
    return {
      login: false
    }
  },
  methods: {
    logout: function () {
      const result = confirm('sure?')
      if (result) {
        localStorage.removeItem('jwt')
        this.login = false
        this.$router.push({name: 'Login'})
      }
    }

  },
  created: function () {
    const token = localStorage.getItem('jwt')

    if (token) {
      this.login = true
    }
  }
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #eff0f1;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #d2d7db;
}
#nav .main_logo {
  width: auto;
  height: 45px;
  margin-right: 1rem
}

#nav a.router-link-exact-active {
  color: #42b983;
}

</style>
