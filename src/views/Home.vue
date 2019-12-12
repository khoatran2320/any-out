<template>
  <div>
    <h1>Home</h1>
    <router-link class="btn btn-outline-primary" to="/signup">
      Sign up
    </router-link>
    <router-link class="btn btn-outline-primary" to="/signin">
      Sign in
    </router-link>
    <router-link class="btn btn-outline-primary" to="/event">
      Event
    </router-link>
    <router-link to="/browse" class="btn btn-outline-primary">
      Browse
    </router-link>
  </div>



</template>
<script>
export default {
  name: "Home"
};
</script>
