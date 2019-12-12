<template>
  <div>
    <div v-if="signupSuccess">
      <b-alert
        variant="success"
        @dismissed="signupFeedback"
        :show="!signupFailed"
        dismissible
      >Signup Successful! Close the banner to log in.</b-alert>
    </div>
    <div v-if="signupFailed">
      <b-alert
        variant="danger"
        @dismissed="signupFeedbackFailed"
        :show="!this.signupSuccess"
        dismissible
      >
        Signup Failed! Maybe you already have an account? Please try
        again.
      </b-alert>
    </div>
    <div id="login-box">
      <div class="left-box">
        <h1>Sign Up</h1>
        <form
          @submit.prevent="signup"
          oninput="password2.setCustomValidity(password2.value != password.value ? 'Passwords do not match.' : '')"
        >
          <input
            type="text"
            name="name"
            id="name"
            placeholder="Full Name"
            class="form-control"
            required
          />
          <input
            pattern="[\w]+@bu\.edu"
            type="email"
            name="email"
            id="email"
            oninvalid="email.setCustomValidity('Please signup with a BU email')"
            oninput="setCustomValidity('')"
            placeholder="Email"
            class="form-control"
            required
          />
          <input
            type="password"
            name="password"
            placeholder="Password"
            class="form-control"
            id="password"
            minlength="6"
            required
          />
          <input
            type="password"
            name="password2"
            placeholder="Confirm Password"
            class="form-control"
            required
          />
          <div class="signupDiv">
            <button type="submit" name="signup-button" class="btn btn-outline-primary">Sign Up</button>
          </div>
        </form>
      </div>
      <div class="right-box">
        <span class="signinwith">Already have an account?</span>
        <div class="signupDiv">
          <button class="btn btn-outline-primary" @click="loginRedirect">Log in</button>
        </div>
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

      this.$router.push("/login");
    },
    signupFeedbackFailed() {
      this.signupFailed = false;

      window.location.reload(true);
    },
    loginRedirect() {
      this.$router.push("/login");
    },
    signup() {
      post("/register", {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        password: document.getElementById("password").value
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
input[type="email"],
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
  padding-top: 5rem;

  display: block;
  margin-bottom: 40px;
  font-size: 28px;
  font-weight: 300;
  text-align: center;
}
.signupDiv {
  margin-top: 0;
  text-align: center;
  width: 100%;
}
</style>
