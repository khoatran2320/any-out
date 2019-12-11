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
        zoom: 14,
        center: { lat: 42.350695, lng: -71.106439 }
      });
      /* eslint-disable no-unused-vars */
      const markers = this.$store.getters["getEvents"].map(location => {
        const marker = new google.maps.Marker({
          position: {
            lat: location["lat"],
            lng: location["lng"]
          },
          map: map
        });
        var infowindow = new google.maps.InfoWindow();
        google.maps.event.addListener(marker, "click", function() {
          infowindow.setContent(
            `<div style="font-weight:700;padding-bottom:0px;text-align:center;font-size:1rem;">${location.content.title}</div><div style="padding-top:.3rem;text-align:center;">${location.content.description}</div><div style="text-align:center; padding-top: .2rem;">Time: ${location.content.startTime} - ${location.content.endTime}</div><div style="text-align:center;"><a href="https://www.google.com/" target="_blank">Learn More</a></div>`
          );
          infowindow.open(map, this);
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