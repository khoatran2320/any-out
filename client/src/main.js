import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import * as VueGoogleMaps from "vue2-google-maps";

Vue.use(VueGoogleMaps, {
  load: {
    key: "AIzaSyBKNJBEeR0YyKxN1L2hZUa5AGxjDGY43eA",
    libraries: "places" // necessary for places input
  }
});

Vue.config.productionTip = false;

new Vue({ router, store, render: h => h(App) }).$mount("#app");
