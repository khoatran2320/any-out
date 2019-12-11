import Vue from "vue";
import Vuex from "vuex";
import { addCookie, wasAlreadyLoggedIn } from "./scripts/authentication";
import { post } from "./scripts/post";

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    loggedIn: wasAlreadyLoggedIn(),

    events: [
      {
        lat: 42.349533,
        lng: -71.099621,
        content: {
          title: "Ayyy Questrom Snakes Let's Link Uppp",
          description:
            "We having our daily business meetings at the Starbucks here in our lair. Come join us and talk about stonks!",
          startTime: "12:00PM",
          endTime: "2:00PM"
        }
      },

      {
        lat: 42.350259,
        lng: -71.105717,
        content: {
          title: "Calculus study sessions",
          description:
            "Join us for a calc 1 study session! There will be pizza and a lot of differential equation practice problems!",
          startTime: "3:00PM",
          endTime: "6:00PM"
        }
      }
    ]
  },
  mutations: {
    setLoggedInTrue(state) {
      state.loggedIn = true;
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
