import Vue from "vue";
import Vuex from "vuex";
import { addCookie, wasAlreadyLoggedIn } from "./scripts/authentication";
import { post, get } from "./scripts/post";

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    loggedIn: wasAlreadyLoggedIn(),
    events: []
  },
  mutations: {
    setLoggedInTrue(state) {
      state.loggedIn = true;
    },
    setEvents(state, events) {
      for (var i = 1; i <= events[0]; i++) {
        state.events.push(events[i]);
      }
    }
  },
  getters: {
    getEvents: state => {
      return state.events;
    },
    isLoggedIn: state => {
      return state.loggedIn;
    }
  },
  actions: {
    /*eslint-disable no-unused-vars*/
    retrieveEvents(state) {
      get("/get-events").then(response => {
        store.commit("setEvents", response.data);
      });
    },
    retrieveSessionID(state, payload) {
      return new Promise((resolve, reject) => {
        post("/login", payload)
          .then(response => {
            addCookie(
              response.data.key,
              response.data.value
              // response.data.expires
            );
            store.commit("setLoggedInTrue");
            resolve(response);
          })
          .catch(error => {
            // eslint-disable-next-line no-console
            console.log(error);
            reject(error);
          });
      });
    }
  }
});

export default store;
