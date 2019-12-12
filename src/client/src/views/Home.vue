<template>
  <div>
    <header class="v-header container">
      <div class="fullscreen-video-wrap">
        <!--  https://www.videvo.net/video/typing-on-computer-white-bg/4475/ -->
        <!-- DO NOT USE THIS VIDEO, I JUST NEEDED A HOSTED VIDEO FOR THIS CODEPEN> USE THE ONE ABOVE -->
        <video autoplay loop>
          <source src="../assets/video.mp4" type="video/mp4" />
        </video>
      </div>
      <div class="header-overlay"></div>
      <div class="header-content text-md-center">
        <h1>Anyout</h1>
        <p>A Place To Host And Join Events, Anyout Is Designed To Help College Students Meet Other Students On Campus</p>
      </div>
    </header>
    <div class="bottom">
      <section class="section section-a">
        <div class="container">
          <img
            src="../assets/host.jpg"
            width="100%"
            height="100%"
            class="d-inline-block align-top"
            alt="Logo"
          />
          <p>Host</p>
        </div>
      </section>

      <section class="section section-b">
        <div class="container">
          <img
            src="../assets/browse.jpg"
            width="100%"
            height="100%"
            class="d-inline-block align-top"
            alt="Logo"
          />
          <p>Browse</p>
        </div>
      </section>
      <section class="section section-c">
        <div class="container">
          <img
            src="../assets/join.jpg"
            width="100%"
            height="100%"
            class="d-inline-block align-top"
            alt="Logo"
          />
          <p>Join</p>
        </div>
      </section>
    </div>
  </div>
</template>
<script>
export default {
  name: "Home"
};
</script>

<style scoped>
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  font-size: 1rem;
  font-weight: normal;
  line-height: 1.5;
  color: #333;
  overflow-x: hidden;
}

.v-header {
  margin-top: 4rem;
  height: 46vh;
  display: flex;
  align-items: center;
  color: #fff;
}

.container {
  margin-top: 4rem;
  max-width: 960px;
  padding-left: 1rem;
  padding-right: 1rem;
  margin: auto;
  text-align: center;
}

.fullscreen-video-wrap {
  position: absolute;
  left: 0;
  width: 100%;
  height: 46vh;
  overflow: hidden;
}

.fullscreen-video-wrap video {
  min-height: 100%;
  min-width: 100%;
}

/* .header-overlay {
  height: 80vh;
  position: absolute;
  left: 0;
  width: 100vw;
  z-index: 1;
  background: #225470;
  opacity: 0.85;
} */

.header-content {
  z-index: 2;
}

.header-content h1 {
  font-size: 50px;
  margin-bottom: 0;
}

.header-content p {
  font-size: 1.5rem;
  display: block;
  padding-bottom: 2rem;
}

.btn {
  background: #34b3a0;
  color: #fff;
  font-size: 1.2rem;
  padding: 1rem 2rem;
  text-decoration: none;
}
.bottom {
  display: flex;
  flex-direction: row;
}
.section {
  padding: 20px 0;
  margin: 0;
  background-color: #e3f2fd;
  color: #333;
}
img {
  padding: 0;
}
p {
  font-size: 2rem;
}
@media (max-width: 960px) {
  .container {
    padding-right: 3rem;
    padding-left: 3rem;
  }
}
</style>