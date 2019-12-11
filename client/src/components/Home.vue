<template>
    <nav id = "wrap">
        <div class = "header">
            <button class = "name"><img class = "image" src = "./Image/LOGO copy.png"></button>
            <button class = "SignIn">SIGN IN</button>
            <button class = "Join">JOIN</button>
        </div>
        <div id = "main">
            <div class = "description"> 
            <h1> WHATEVER </h1>
            </div>
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
  width: 102%; height: 60px;
  background-color: #173F5F; 
}

.image{
    width: 50px; height: 50px;
}

.name{
    background-color: #173F5F; margin-top: 3px; 
    border: none; margin-left: 5%;
}

.SignIn{
    background-color: #173F5F; color: #3CAEA3;
    margin-top: 3px; width: 130px; height: 50px; font-size: 19px;
    border: none; font-weight: 700; margin-left: 60%;
    text-decoration-line: underline; 
}

.Join{
    background-color: #173F5F; color: #ED553B;
    margin-top: 0px; width: 80px; height: 50px; font-size: 19px; 
    border: none; font-weight: 700; margin-left: 0.5%; margin-right: 0;
    text-decoration-line: underline;
}

#main{
}

.description{
    margin-left: 50%;
}

.desc{

}

h1{
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;

}

</style>