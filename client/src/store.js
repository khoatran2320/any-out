import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    events: [
      { lat: 42.3601, lng: -71.0589 },
      {
        lat: 42.4668,
        lng: -70.9495,
        content: "Abdel is gay"
      }
    ]
  },
  mutations: {},
  getters: {
    getEvents: state => {
      return state.events;
    }
  },
  actions: {}
});

export default store;
