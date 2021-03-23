<template>
  <div class="wrapper">
    <h2>최신작</h2>
    <Latest :Latest="LatestList" />
    <h2>인기작</h2>
    <Popular :Popular="PopularList" />
    <h2>고전 명작</h2>
    <Classic :Classic="ClassicList" />
  </div>
</template>

<script>
import { Glide, GlideSlide } from 'vue-glide-js'
import Latest from '@/components/Home/Latest.vue'
import Popular from '@/components/Home/Popular.vue'
import Classic from '@/components/Home/Classic.vue'

export default {
  name: 'Carousel',
  components: {
    [Glide]: Glide,
    [GlideSlide]: GlideSlide,
    Latest,
    Popular,
    Classic,
  },
  data: function () {
    return {
      active: 0,
      LatestList: this.$store.state.LatestList,
      PopularList: this.$store.state.PopularList,
      ClassicList: this.$store.state.ClassicList,
    }
  },
  computed: {
  },
  methods: {
    
  },
}
</script>

<style>

.wrapper {
  display: grid;
  overflow: hidden;
  scroll-behavior: smooth;
}
.wrapper section {
  width: 100%;
  position: relative;
  overflow: hidden;
  white-space: nowrap;
  display: flex;
  align-items: center;
  margin: 20px 0;
}
.wrapper section .item {
  padding: 0 3px;
  width: auto;
  height: 350px;
}
.wrapper section .item:hover {
  margin: 0 40px;
  transform: scale(1.2);
}
.arrow {
  position: absolute;
  color: #fff;
  text-decoration: none;
  font-size: 6em;
  background: #000;
  width: 80px;
  padding: 20px;
  text-align: center;
  z-index: 3;
}
.arrow:hover {
  cursor: pointer;
  text-decoration: none;
  color: rgba(206, 200, 200, 0.432)
}
.wrapper section img {
  background-size: cover;
  cursor: pointer;
  width: auto;
  height: 100%;
  z-index: 2;
}
.wrapper section a:nth-of-type(1) {
  top: 3rem;
  bottom: 0;
  left: 0;
  background: linear-gradient(-90deg, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 1) 100%);
}
.wrapper section a:nth-of-type(2) {
  top: 3rem;
  bottom: 0;
  right: 0;
  background: linear-gradient(90deg, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 1) 100%);
}
 @media only screen and (max-width: 600px) {
   .carousel a.arrow__btn {
     display: none;
	}
}
</style>