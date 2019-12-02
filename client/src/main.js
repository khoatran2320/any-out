import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import * as VueGoogleMaps from "vue2-google-maps";

Vue.use(VueGoogleMaps, {
  load: {
    key: "AIzaSyD-cJN2NB2GEhiDcb7MWji727_ckh0bfCI",
    libraries: "places" // necessary for places input
  }
});

Vue.config.productionTip = false;

new Vue({ router, store, render: h => h(App) }).$mount("#app");
