<template>
  <div id="app">
    <router-view>
      <router-link to="/"></router-link>
    </router-view>
  </div>
</template>

<script>
// import Home from "./views/Home.vue";
export default {
  name: "app"
  // components: { Home }
};
</script>