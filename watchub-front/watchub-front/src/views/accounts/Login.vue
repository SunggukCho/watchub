<template>
  <div>
    <h1>Login</h1>
      <div>
        <label for="username">사용자이름: </label>
        <input type="text" required id="username" placeholder="username"
        v-model="credentials.username">
      </div>
      <div>
        <label for="password">비밀번호: </label>
        <input type="password" required id="password" placeholder="password"
        v-model="credentials.password"
        @keypress.enter="login">
      </div>
      <button @click="login">로그인</button>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
      username: '',
      password: '',
      passwordConfirmation: '',
      }
    }
  },
  methods: {
    login: function () {
      axios.post(`${SERVER_URL}/accounts/api-token-auth/`, this.credentials)
      .then((res) => {
        localStorage.setItem('username', this.credentials.username)
        localStorage.setItem('jwt', res.data.token)
        // localStorage.setItem('user_id', res.data.)
        this.$emit('login')
        this.$router.push({name: 'Recommend'})
      })
      .catch((err) => {
        console.log(err)
      })
      axios.post(`${SERVER_URL}/accounts/login/`, this.credentials)
      .then((res) => {
        const userId = res.data.userId
        localStorage.setItem('user_id', userId)
        this.$store.commit('SET_USER_ID', userId)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>