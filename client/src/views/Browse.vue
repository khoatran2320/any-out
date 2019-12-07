<template>
  <div>
    <h1>Browse</h1>
    <GoogleMap />
  </div>
</template>

<script>
import GoogleMap from "../components/GoogleMap.vue";

export default {
  name: "browse",
  components: {
    GoogleMap
  }
};
</script>
<style scoped>
h1 {
  margin-left: 1rem;
}
</style>