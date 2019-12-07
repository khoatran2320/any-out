import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
// import * as VueGoogleMaps from "vue2-google-maps";

// Vue.use(VueGoogleMaps, {
//   load: {
//     key: "",
//     libraries: "places" // necessary for places input
//   }
// });

Vue.config.productionTip = false;

new Vue({ router, store, render: h => h(App) }).$mount("#app");
