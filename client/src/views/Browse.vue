<template>
  <div>
    <div class = "header">
            <router-link to="/" class = "btn btn-outline-primary Logo"><img class = "image" src = "./Image/LOGO.png"></router-link>
            <router-link to="/signin" class = "btn btn-outline-primary SignIn">SIGN IN</router-link>
            <router-link class="btn btn-outline-primary Join" to="/signup">JOIN</router-link>
    </div>
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
  margin-top: 20px; 
  margin-left: 10px;
}

.header{
  margin: -8px -10px -10px -10px;
  width: 102%; height: 70px;
  background-color: #173F5F; 
}

.image{
    width: 50px; height: 50px;
}

.Logo{
    background-color: #173F5F; margin-top: 8px; 
    border: none; margin-left: 5%;
}

.SignIn{
    background-color: none; color: #3CAEA3; float: right;
    margin-top: 20px; width: 100px; height: 45px; font-size: 19px;
    border: none; font-weight: 700; margin-right: 2%;
}

.Join{
    background-color: #173F5F; color: #ED553B; float: right;
    margin-top: 20px; width: 80px; height: 45px; font-size: 19px; 
    border: none; font-weight: 700; margin-right: 0.3%; margin-right: 0;
}

</style>