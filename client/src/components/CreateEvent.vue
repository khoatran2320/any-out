<template>
  <div>
    <div>
      <b-alert
        variant="success"
        @dismissed="submitFeedback"
        :show="submitSuccess"
        dismissible
      >Successfully created event! Close the banner to return to home page.</b-alert>
      <b-alert
        variant="danger"
        @dismissed="submitFeedbackFailed"
        :show="submitFailed"
        dismissible
      >Failed to create event! Please try again.</b-alert>
    </div>
    <div id="AddEvent">
      <h2>Create Your Event</h2>
      <form @submit.prevent="createEventSubmit">
        <label for="event-title">Title:</label>
        <input
          id="event-title"
          type="text"
          class="form-control"
          required
          placeholder="What's the Name of Your Event?"
          v-model="title"
          autofocus
        />
        <label for="event-description">Event Description</label>
        <textarea
          id="event-description"
          type="text"
          class="form-control"
          v-model="description"
          required
          placeholder="Describe Your Event"
        ></textarea>
        <label for="event-location">Location:</label>
        <input
          id="event-location"
          type="text"
          class="form-control"
          required
          v-model="location"
          ref="eventLocation"
          placeholder="Where Are You Hosting Your Event?"
        />
        <div class="start-end-time">
          <div class="time">
            <label for="event-time-start">Start Time:</label>
            <input
              id="event-time-start"
              v-model="startTime"
              type="time"
              class="form-control"
              required
              placeholder="06:30 PM"
            />
          </div>
          <div class="time">
            <label for="event-time-end">End Time:</label>
            <input id="event-time-end" v-model="endTime" type="time" class="form-control" required />
          </div>
        </div>

        <label for="event-capacity">Capacity:</label>
        <input id="event-capacity" v-model="capacity" type="number" class="form-control" required />
        <div class="button-container">
          <button type="submit" class="btn btn-outline-primary create-button">Create Event</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import gmapsInit from "../scripts/gmaps";
import { post } from "../scripts/post";
export default {
  name: "createEvent",
  async mounted() {
    const google = await gmapsInit();
    /*eslint-disable no-undef*/
    this.autocomplete = new google.maps.places.Autocomplete(
      this.$refs.eventLocation,
      { types: ["geocode"] }
    );
    this.autocomplete.addListener("place_changed", () => {
      let place = this.autocomplete.getPlace();
      let ac = place.address_components;
      let lat = place.geometry.location.lat();
      let lng = place.geometry.location.lng();
      let address =
        ac[0]["short_name"] +
        " " +
        ac[1]["short_name"] +
        ", " +
        ac[3]["short_name"] +
        ", " +
        ac[5]["short_name"] +
        ", " +
        ac[7]["short_name"];
      /*eslint-disable no-console*/
      this.address = address;
      this.lat = lat;
      this.lng = lng;
    });
  },
  data() {
    return {
      address: "",
      lat: "",
      lng: "",
      submitSuccess: false,
      submitFailed: false
    };
  },
  methods: {
    submitFeedback() {
      this.submitSuccess = false;

      this.$router.push("/");
    },
    submitFeedbackFailed() {
      this.signupFailed = false;

      window.location.reload(true);
    },
    createEventSubmit() {
      post("/createEvent", {
        address: this.address,
        lat: this.lat,
        lng: this.lng,
        description: this.description,
        title: this.title,
        capacity: this.capacity,
        startTime: this.startTime,
        endTime: this.endTime
        /* eslint-disable no-unused-vars*/
      })
        .then(res => {
          document.getElementById("event-title").value = "";
          document.getElementById("event-description").value = "";
          document.getElementById("event-location").value = "";
          document.getElementById("event-time-start").value = "";
          document.getElementById("event-time-end").value = "";
          document.getElementById("event-capacity").value = "";
          this.submitSuccess = true;
          this.submitFailed = false;
        })
        .catch(err => {
          this.submitSuccess = false;
          this.submitFailed = true;
        });
    }
  }
};
</script>

<style>
#AddEvent * {
  box-sizing: border-box;
}
#AddEvent {
  margin: 20px auto;
  max-width: 500px;
}
label {
  display: block;
  margin: 20px 0 10px;
}
input[type="text"],
textarea {
  display: block;
  width: 100%;
  padding: 8px;
}
#preview {
  padding: 10px 20px;
  border: 1px dotted #ccc;
  margin: 30px 0;
}
h3 {
  margin-top: 10px;
}
.button-container {
  text-align: center;
}
.create-button {
  margin-top: 1.5rem;
}

.start-end-time {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
.time {
  display: flex;
  flex-direction: column;

  width: 48%;
}
</style>