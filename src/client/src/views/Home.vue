<template>
  <div>
    <h1>Home View</h1>
    <router-link class="btn btn-outline-primary" to="/signup">Signup</router-link>
    <router-link to="/browse" class="btn btn-outline-primary">Browse</router-link>
    <router-link to="/create-event" class="btn btn-outline-primary">Create Event</router-link>
  </div>
</template>
<script>
export default {
  name: "Home"
};
</script>
