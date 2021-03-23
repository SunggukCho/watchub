import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Recommend from '../views/Recommend.vue'
import MyMovie from '../views/MyMovie.vue'
import RecommendCarousel from '../views/RecommendCarousel.vue'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import WishList from '@/components/MyMovie/Wishlist'
import Favorite from '@/components/MyMovie/Favorite'
import Already from '@/components/MyMovie/Already'
import VueGlide from 'vue-glide-js'
import 'vue-glide-js/dist/vue-glide.css'

Vue.use(VueRouter)
Vue.use(VueGlide)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/recommend',
    name: 'Recommend',
    component: Recommend
  },
  {
    path: '/recommendcarousel',
    name: 'RecommendCarousel',
    component: RecommendCarousel
  },
  {
    path: '/mymovie',
    name: 'MyMovie',
    component: MyMovie
  },
  {
    path: '/mymovie/wishlist',
    name: 'WishList',
    component: WishList
  },
  {
    path: '/mymovie/favorite',
    name: 'Favorite',
    component: Favorite
  },
  {
    path: '/mymovie/already',
    name: 'Already',
    component: Already
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
