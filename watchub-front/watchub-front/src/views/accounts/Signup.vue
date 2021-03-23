<template>
  <div>
    <h1>signup</h1>
    <div>
      <label for="username">사용자이름: </label>
      <input type="text" required id="username" minlength="3" maxlength="10" placeholder="username"
      v-model="credentials.username">
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="password" required id="password" minlength="8" maxlength="16" placeholder="password"
      v-model="credentials.password">
    </div>
    <div>
      <label for="passwordConfirmation">비밀번호 확인: </label>
      <input type="password" required id="passwordConfirmation" minlength="8" maxlength="16" placeholder="password"
      v-model="credentials.passwordConfirmation"
      @keypress.enter="signup">
    </div>
    <button @click="signup">회원가입</button>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Singup',
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
    signup: function () {
      axios.post(`${SERVER_URL}/accounts/signup/`, this.credentials)
      .then((res) => {
        console.log(res)
        this.$router.push({name: 'Login'})
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>