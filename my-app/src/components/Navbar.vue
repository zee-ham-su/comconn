<template>
  <nav>
    <router-link to="/">Home</router-link>
    <router-link to="/resources">Resources</router-link>
    <router-link to="/reviews">Reviews</router-link>
    <!-- Add more navigation links as needed -->
  </nav>
</template>

<script>
export default {
  name: 'MyNavbar',
};
</script>

<style scoped>
/* Add styling for your Navbar */
nav {
  background-color: #42b983;
  padding: 10px;
  text-align: center;
}

router-link {
  margin: 0 10px;
  color: #ffffff;
  text-decoration: none;
  font-weight: bold;
  font-size: 16px;
}
</style>
