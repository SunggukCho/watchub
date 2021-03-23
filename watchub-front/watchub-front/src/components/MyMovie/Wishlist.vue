<template>
  <div id="WishList">
    <div class="nav">
      <router-link :to="{name: 'Favorite'}" class="innerLink"> 좋아하는 영화</router-link> |
      <router-link :to="{name: 'Already'}" class="innerLink"> 본 영화</router-link> |
      <router-link :to="{name: 'WishList'}" class="innerLink"> 나중에 볼 영화</router-link> 
    </div>
    <hr>
    <h3>보고 싶은 영화 목록을 추가하세요!</h3>
      <input type="text" v-model="tempWish" @keypress.enter="createWishList" size="60">
      <button @keypress.enter="createWishList">추가하기</button>
      <ul v-for="(wish, idx) in wishList" :key="idx">
        <li v-if="wish.completed === false" > 
          <!-- 본 영화는 안보여주기 completed===false -->
          {{ wish.title }}
        </li>
      </ul>
  </div>
</template>

<script>

export default {
  name: 'WishList',
  components: {
  },
  data: function () {
    return {
      tempWish: '',
    }
  },
  computed: {
    wishList: function () {
      return this.$store.state.wishList
    }
  },
  methods: {
    createWishList: function () {
      this.wishes = {title: this.tempWish, completed: false}
      this.$store.dispatch('getWishList', this.wishes)
      this.tempWish = ''
    }
  }
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
#WishList{
  text-align: center;
}
.innerLink {
  color: #fff;
  font-size: 2rem;
  font-size: 1rem;
}
li {
  list-style: none;
}
</style>