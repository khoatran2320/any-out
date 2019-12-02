<template>
  <div>
    <h1>Home Page</h1>

    <router-link to="/login">Login</router-link>
    <router-link to="/browse">Browse</router-link>
    <router-view></router-view>
  </div>
</template>
<script>
export default {
  name: "Home"
};
</script>