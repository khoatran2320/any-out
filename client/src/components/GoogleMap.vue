<template>
  <div class="App" />
</template>

<script>
import gmapsInit from "../scripts/gmaps";

export default {
  name: "GoogleMap",
  async mounted() {
    try {
      const google = await gmapsInit();
      // const geocoder = new google.maps.Geocoder();
      const map = new google.maps.Map(this.$el, {
        zoom: 8,
        center: { lat: 42.3601, lng: -71.0589 }
      });

      // geocoder.geocode({ address: "Boston" }, (results, status) => {
      //   if (status !== "OK" || !results[0]) {
      //     throw new Error(status);
      //   }

      //   map.setCenter(results[0].geometry.location);
      //   map.fitBounds(results[0].geometry.viewport);
      // });
      /* eslint-disable no-unused-vars */
      // google.maps.event.addListener(map, "click", function(event) {
      //   // Add marker
      //   var marker = new google.maps.Marker({
      //     position: event.latLng,
      //     map: map
      //     //icon:props.iconImage
      //   });
      // });
      // // eslint-disable-next-line no-console
      // console.log(this.$store.getters["getEvents"][0]["lat"]);
      // // eslint-disable-next-line no-console
      // console.log(this.$store.getters["getEvents"][0]["lng"]);

      // const marker = new google.maps.Marker({
      //   position: {
      //     lat: this.$store.getters["getEvents"][0]["lat"],
      //     lng: this.$store.getters["getEvents"][0]["lng"]
      //   },
      //   map: map
      // });

      const markers = this.$store.getters["getEvents"].map(location => {
        const marker = new google.maps.Marker({
          position: {
            lat: location["lat"],
            lng: location["lng"]
          },
          map: map
        });

        marker.addListener(`click`, () => {
          var infoWindow = new google.maps.InfoWindow({
            content: location.content
          });
          infoWindow.open(map, marker);
        });
        return marker;
      });
    } catch (error) {
      // console.error(error);
    }
  }
};
</script>

<style>
html,
body {
  margin: 0;
  padding: 0;
}

.App {
  width: 60vw;
  height: 90vh;
  border-radius: 1%;
}
</style>