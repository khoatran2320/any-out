<template>
  <div id="app">
    <nav
      class="navbar navbar-expand-lg navbar-light"
      style="background-color: #e3f2fd; padding:0; display:flex;justify-content:space-between; height:4rem;"
    >
      <a class="navbar-brand" style="margin-left: 1rem;margin-top:0;padding:0" href="/">
        <img
          src="./assets/LOGO.png"
          width="60"
          height="60"
          class="d-inline-block align-top"
          alt="Logo"
        />
      </a>
      <div v-if="!this.$store.getters['isLoggedIn']">
        <li style="display:flex;justify-content:space-around;width:10rem;margin-right:2rem;">
          <router-link to="/signup" class="btn btn-outline-primary">Sign up</router-link>
          <router-link to="/login" class="btn btn-outline-primary">Log in</router-link>
        </li>
      </div>
      <div
        v-if="this.$store.getters['isLoggedIn']"
        style="display:flex;width:22rem;justify-content:space-around; margin-right: 2rem"
      >
        <button @click="browse" class="btn btn-outline-primary">Browse Events</button>
        <router-link to="/create-event" class="btn btn-outline-primary">Create Event</router-link>
        <button class="btn btn-outline-primary" @click="logoutButton">Log out</button>
      </div>
    </nav>
    <router-view>
      <router-link to="/"></router-link>
    </router-view>
  </div>
</template>

<script>
import { deleteCookie } from "./scripts/authentication";
export default {
  name: "app",
  methods: {
    browse() {
      this.$router.push("/browse");
      this.$store.dispatch("retrieveEvents");
    },

    logoutButton() {
      deleteCookie("SID");
      this.$router.push("/");
      window.location.reload(true);
    }
  }
};
</script>
