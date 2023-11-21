<template>
  <nav>
    <ul>
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/resources">Resources</router-link></li>
      <li><router-link to="/reviews">Reviews</router-link></li>
      <!-- Add more links as needed -->
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'NavigationBar',
};
</script>

<style scoped>
/* Add styling for your navigation bar */
nav {
  background-color: #333;
  color: white;
  padding: 10px;
}

ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  display: flex;
}

li {
  margin-inline-end: 15px;
}

a {
  text-decoration: none;
  color: white;
  font-weight: bold;
}
</style>
