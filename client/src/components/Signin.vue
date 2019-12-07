<template>
<nav id = "wrap">
<div id = "header">
<button class = "name">ANY OUT</button>
</div>
  <div id="login-box">
    <div class="left-box">
      <h1>Sign In</h1>
      <form action = "loginaction.php">
      <input type="text" name="username" placeholder="Username" />
      <input type="text" name="email" placeholder="Password" />
      <input type="submit" name="signup-button" value="SIGN IN" />
      </form>
    </div>
    <div class="right-box">
      <span class="signupwith">Do You Need An Account?</span>
      <button class="sign-up">REGISTER</button>
    </div>
    <div class="or">OR</div>
  </div>
  </nav>
</template>
<script>
export default {
  name: "Signin"
};
</script>
<style scoped>
body {
  margin: 0;
  padding: 0;
  background: #ededed;
  font-size: 16px;
  color: #777;
  font-family: sans-serif;
  font-weight: 300;
}
#header{
  position: relative; 
  margin: -10px -10px -10px -10px;
  width: 102%; height: 60px;
  background-color: #173F5F; 
}

.name{
  margin: 0 auto; background-color: #173F5F;
  color: white; margin-top: 15px; 
  width: 150px; height: 50x; font-size: 20px;
  border: none; font-weight: 900; margin-left: 45%;
}

#login-box {
  position: relative;
  margin: 10% auto;
  height: 300px;
  width: 600px;
  background: #ededed;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.6);
}
.left-box {
  position: absolute;
  top: 0;
  left: 0;
  box-sizing: border-box;
  padding: 40px;
  width: 300px;
  height: 400 px;
}
h1 {
  margin: 0 0 20px 62px;
  font-weight: 700;
  font-size: 28px;
  color: #173F5F;
  font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
}
input[type="text"],
input[type="password"] {
  display: block;
  box-sizing: border-box;
  margin-bottom: 20px;
  padding: 4px;
  width: 220px;
  height: 32px;
  border: none;
  outline: none;
  border: 1px solid #aaa;
  background: #ededed;
  font-family: sans-serif;
  font-weight: 400;
  font-size: 15px;
  transition: 0.2s ease;
}
input[type="submit"] {
  margin-bottom: 28px;
  margin-left: 50px;
  margin-top: 10px;
  width: 120px;
  height: 32px;
  background: #ED553B;
  border: none;
  border-radius: 2px;
  color: #fff;
  font-family: sans-serif;
  font-weight: 500;
  text-transform: uppercase;
  transition: 0.2s ease;
  cursor: pointer;
}
input[type="submit"]:hover,
input[type="submit"]:focus {
  background: #bee2e7;
  transition: 0.2s ease;
}
.right-box {
  position: absolute;
  top: 0;
  right: 0;
  box-sizing: border-box;
  padding: 40px;
  width: 300px;
  height: 400px;
  /* background-image: url(./images/pic1.jpg); */
  background-size: cover;
  background-position: center;
}
.or {
  position: absolute;
  top: 150px;
  left: 290px;
  width: 40px;
  height: 40px;
  background: #F6D55C;
  border-radius: 50%;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.6);
  line-height: 40px;
  text-align: center;
  font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
}
.right-box .signupwith {
  display: block;
  margin-bottom: 40px;
  font-size: 28px;
  color: #173F5F;
  text-align: center;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.6);
  font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
}
button.sign-up {
  margin-bottom: 20px;
  margin-top: 15px;
  margin-left: 55px;
  width: 100px;
  height: 36px;
  border: none;
  border-radius: 2px;
  color: #fff;
  font-family: sans-serif;
  font-weight: 500;
  transition: 0.2s ease;
  cursor: pointer;
  background-color: #ED553B;
}
</style>