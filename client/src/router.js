import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";

Vue.use(Router);

const router = new Router({
  mode: "history",

  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/login",
      name: "login",
      component: () => import("./components/Signin.vue")
    },
    {
      path: "/browse",
      name: "browse",
      component: () => import("./views/Browse.vue")
    }
  ]
});

export default router;
