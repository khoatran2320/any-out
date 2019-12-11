<template>
    <nav id = "wrap">
        <div class = "header">
            <router-link to="/" class = "btn btn-outline-primary Logo"><img class = "image" src = "./Image/LOGO.png"></router-link>
            <router-link to="/signin" class = "btn btn-outline-primary SignIn">SIGN IN</router-link>
            <router-link class="btn btn-outline-primary Join" to="/signup">JOIN</router-link>
        </div>
        <div id = "main">
            <h1> ANY OUT </h1>
            <h2> Find people around you and join them! </h2>
            <router-link to="/browse" class="btn btn-outline-primary Browse">Browse</router-link>
            <router-link to="/create-event" class="btn btn-outline-primary Create">Create Event</router-link>
        </div>
    </nav>
</template>

<script>
export default {
name: 'Home'
}
</script>

<style scoped>
body{
  margin: 0;
  padding: 0;
  color: #777;
  font-weight: 300;
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

#main{
  margin-top: 10%;
}

.Browse{
  margin-top: 5%; position: absolute; left: 50%; border: none; color: #404040; text-align: center;
  width: 100px; height: 45px; font-weight: 600; font-size: 22px; background-color: #e6e3da;
}

.Create{
  margin-top: 5%; margin-left: 0.5%; border: none; color: #404040;
  width: 155px; height: 45px; font-weight: 600; font-size: 22px; background-color: #e6e3da;
  
}

h1{
    text-align: center;
    text-shadow: 0 2px 4px #969696;
    color: #004215;
    font-size: 50px;
    font-style: italic;
}

h2{
  text-align: center;
  font-size: 27px;
  margin-top: 20px;
}

.btn-outline-primary:hover{
  color: red;
  text-decoration-line: underline;
}
.btn-outline-primary:active{
  color: none;
}

</style>
