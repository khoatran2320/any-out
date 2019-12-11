<template>
  <div>
    <div v-if="resetSuccess">
      <b-alert
        variant="success"
        @dismissed="resetFeedback"
        :show="!resetFailed"
        dismissible
      >Reset Password Successful! Close the banner to return to home page.</b-alert>
    </div>
    <div v-if="resetFailed">
      <b-alert
        variant="danger"
        @dismissed="resetFeedbackFailed"
        :show="!this.resetSuccess"
        dismissible
      >Reset Password Failed! Please try again.</b-alert>
    </div>
    <div class="reset-box">
        <h1>Reset Your Password</h1>
        <form
          @submit.prevent="reset"
        >
          <input
            type="password"
            name="oldpassword"
            v-model="password"
            placeholder="Enter old password"
            class="form-control"
            required
          />
          <input
            type="password"
            name="newpassword"
            placeholder="Enter new password"
            class="form-control"
            required
          />
          <input
            type="password"
            name="newpassword2"
            placeholder="Confirm new password"
            class="form-control"
            required
          />
        <button type="submit" name="reset-button" class="btn btn-outline-primary">Reset</button>
        </form>
      </div>   
  </div>
</template>

<script>
import { post } from "../scripts/post";

export default {
  name: "reset",
  data: function() {
    return {
      resetSuccess: false,
      resetFailed: false
    };
  },
  methods: {
    resetFeedback() {
      this.resetSuccess = false;

      this.$router.push("/");
    },
    resetFeedbackFailed() {
      this.resetFailed = false;

      window.location.reload(true);
    },
    lognin() {
      post("/register", {
        password: this.password
        /* eslint-disable no-unused-vars */
      })
        .then(response => {
          this.resetSuccess = true;
          this.resetFailed = false;
        })
        .catch(err => {
          this.resetSuccess = false;
          this.resetFailed = true;
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

.reset-box {
  position: relative;
  margin: 5% auto;
  top: 150px;
  height: 400px;
  width: 400px;
  background: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.6);
}

h1 {
  position: relative;
  top: 40px;
  left: 80px;
  margin: 0 0 20px 0;
  font-weight: 200;
  font-size: 28px;
}
input[type="password"],

input[type="password"] {
  position: relative;
  top: 50px;
  left: 80px;
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

button[type="submit"] {
  position: relative;
  top: 70px;
  left: 145px;
  margin-bottom: 20px;
  width: 100px;
  height: 32px;
  background: #A19386;
  border: none;
  border-radius: 2px;
  color: #fff;
  font-family: sans-serif;
  font-weight: 500;
  text-transform: uppercase;
  cursor: pointer;
}

input[type="submit"]:focus {
  background: #bee2e7;
  transition: 0.2s ease;
}
</style>
