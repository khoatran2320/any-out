<template>
    <nav id = "wrap">
        <div class = "header">
            <button class = "name">ANY OUT</button>
            <button class = "SignIn">SIGN IN</button>
            <button class = "Join">JOIN</button>
        </div>
        <div class = "main">
            <div class = "logo">
            <img src="client/src/LOGO.jpg">
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
#logo{
    position: relative; 
  margin: -10px -10px -10px -10px;
  width: 102%; height: 50px;
  background-color: #173F5F; 
}

.name{
    margin: 0 auto; background-color: #173F5F;
    color: white; margin-top: 15px; 
    width: 150px; height: 50x; font-size: 20px;
    border: none; font-weight: 900; margin-left: 3%;
}

.SignIn{
    background-color: #173F5F; color: #3CAEA3;
    margin-top: 15px; width: 150px; height: 50px; font-size: 19px;
    border: none; font-weight: 700; margin-left: 70%; 
    text-decoration-line: underline; font-style: italic;
}

.Join{
    background-color: #173F5F; color: #ED553B;
    margin-top: 15px; width: 100px; height: 50px; font-size: 19px; 
    border: none; font-weight: 700; margin-left: 85%;
    font-style: italic; text-decoration-line: underline;
}

</style>