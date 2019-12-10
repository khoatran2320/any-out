<template>
  <div>
    <h1>Home View</h1>
    <router-link class="btn btn-outline-primary" to="/signup">
      Signup
    </router-link>
    <router-link to="/browse" class="btn btn-outline-primary"
      >Browse</router-link
    >

  </div>
</template>
<script>
export default {
  name: "Home"
};
</script>
