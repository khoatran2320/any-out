<template>
    <div class="resetpasswordDiv">
        <button class="btn btn-outline-primary" @click="ResetPasswordRedirect">Reset Password</button>
    </div>
</template>

<script>


export default {
  name: "resetPassword",
  data: function() {
    return {
      resetpasswordSuccess: false,
      resetpasswordFailed: false
    };
  },
    methods: {
        ResetPasswordRedirect() {
        this.$router.push("/resetpassword");
        }
    }
};
</script>

<style>
.resetpasswordDiv{
  position: relative;
  top: 400px;
  margin-top: 0;
  text-align: center;
  width: 100%;
}
</style>