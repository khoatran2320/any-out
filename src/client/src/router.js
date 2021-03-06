import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import store from "./store";
Vue.use(Router);

// const redirectIfLoggedIn = function(next) {
//   if (store.getters.isLoggedIn) {
//     next("dashboard");
//   } else {
//     next();
//   }
// };

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
      // beforeEnter: (to, from, next) => redirectIfLoggedIn(next)
    },
    {
      path: "/browse",
      name: "browse",
      component: () => import("./views/Browse.vue"),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: "/create-event",
      name: "create-event",
      component: () => import("./components/CreateEvent.vue"),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: "/login",
      name: "login",
      component: () => import("./views/Login.vue")
    }
  ]
});
router.beforeEach((to, from, next) => {
  let auth = store.getters.isLoggedIn;

  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (auth) {
      next();
    } else {
      next({
        path: "/login",
        query: { redirect: to.fullPath }
      });
    }
  } else {
    next();
  }
});
export default router;
