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
        style="display:flex;width:28rem;justify-content:space-between;"
      >
        <router-link to="/browse" class="btn btn-outline-primary">Browse Events</router-link>
        <router-link to="/create-event" class="btn btn-outline-primary">Create Event</router-link>
        <li class="nav-item dropdown form-inline my-1 my-lg-0">
          <button
            class="btn btn-outline-primary nav-link dropdown-toggle"
            id="navbarDropdown"
            data-toggle="dropdown"
            aria-haspopup="true"
            aria-expanded="false"
            style="margin-right:5rem;"
          >User</button>
          <div class="dropdown-menu" aria-labelledby="navbarDropdown">
            <button class="dropdown-item">Account</button>
            <button class="dropdown-item" @click="logoutButton">Log out</button>
          </div>
        </li>
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
    logoutButton() {
      deleteCookie("SID");
      this.$router.push("/");
      window.location.reload(true);
    }
  }
};
</script>
