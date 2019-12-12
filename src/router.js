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
      path: "/signup",
      name: "signup",
      component: () => import("./components/Signup.vue")
    },
    {
      path: "/event",
      name: "event",
      component: () => import("./components/Event.vue")
    },
    {
      path: "/browse",
      name: "browse",
      component: () => import("./views/Browse.vue")
    }
  ]
});

export default router;
