<template>
  <div>
    <div v-if="signupSuccess">
      <b-alert
        variant="success"
        @dismissed="signupFeedback"
        :show="!signupFailed"
        dismissible
        >Signup Successful! Close the banner to return to home page.</b-alert
      >
    </div>
    <div v-if="signupFailed">
      <b-alert
        variant="danger"
        @dismissed="signupFeedbackFailed"
        :show="!this.signupSuccess"
        dismissible
        >Signup Failed! Please try again.</b-alert
      >
    </div>
    <div id="login-box">
      <div class="left-box">
        <h1>Sign Up</h1>
        <form @submit.prevent="signup">
          <input
            type="text"
            name="username"
            v-model="username"
            placeholder="Username"
          />
          <input type="text" name="email" v-model="email" placeholder="Email" />
          <input
            type="password"
            name="password"
            v-model="password"
            placeholder="Password"
          />
          <button type="submit" name="signup-button">Sign Up</button>
        </form>
      </div>
      <div class="right-box">
        <span class="signinwith">Already have an account?</span>
        <button class="sign-in">sign in</button>
      </div>
      <div class="or">OR</div>
    </div>
  </div>
</template>
<script>
import { post } from "../scripts/post";

export default {
  name: "Signup",
  data: function() {
    return {
      signupSuccess: false,
      signupFailed: false
    };
  },
  methods: {
    signupFeedback() {
      this.signupSuccess = false;

      this.$router.push("/");
    },
    signupFeedbackFailed() {
      this.signupFailed = false;

      window.location.reload(true);
    },
    signup() {
      post("/register", {
        username: this.username,
        email: this.email,
        password: this.password
        /* eslint-disable no-unused-vars */
      })
        .then(response => {
          this.signupSuccess = true;
          this.signupFailed = false;
        })
        .catch(err => {
          this.signupSuccess = false;
          this.signupFailed = true;
        });
    }
  }
};
</script>
<style scoped>
body {
  margin: 0;
  padding: 0;
  background: #efefef;
  font-size: 16px;
  color: #777;
  font-family: sans-serif;
  font-weight: 300;
}

#login-box {
  position: relative;
  margin: 5% auto;
  height: 400px;
  width: 600px;
  background: #fff;
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
  margin: 0 0 20px 0;
  font-weight: 300;
  font-size: 28px;
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
  border-bottom: 1px solid #aaa;
  font-family: sans-serif;
  font-weight: 400;
  font-size: 15px;
  transition: 0.2s ease;
}

input[type="submit"] {
  margin-bottom: 28px;
  width: 120px;
  height: 32px;
  background: #9edceb;
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
  top: 180px;
  left: 280px;
  width: 40px;
  height: 40px;
  background: #efefef;
  border-radius: 50%;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.6);
  line-height: 40px;
  text-align: center;
}

.right-box .signinwith {
  display: block;
  margin-bottom: 40px;
  font-size: 28px;
  color: #fff;
  text-align: center;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.6);
}

button.sign-in {
  margin-bottom: 20px;
  width: 100px;
  height: 36px;
  border: none;
  border-radius: 2px;
  color: #fff;
  font-family: sans-serif;
  font-weight: 500;
  transition: 0.2s ease;
  cursor: pointer;
  background-color: #d4bba9;
}
</style>
