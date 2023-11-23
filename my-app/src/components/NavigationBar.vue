<template>
  <nav class="navbar">
    <ul class="nav-list">
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/resources">Resources</router-link></li>
      <li><router-link to="/reviews">Reviews</router-link></li>
      <li><router-link to="/user">User Profile</router-link></li>
      <li><router-link to="/login">Login Page</router-link></li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'NavigationBar',
};
</script>

<style scoped>
/* Updated styling for your navigation bar */
.navbar {
  background-color: #2c3e50;
  /* Dark blue-gray */
  color: white;
  padding: 10px;
}

.nav-list {
  list-style-type: none;
  margin: 0;
  padding: 0;
  display: flex;
}

.nav-list li {
  margin-inline-end: 15px;
}

.nav-list a {
  text-decoration: none;
  color: white;
  font-weight: bold;
  transition: color 0.3s ease;
  /* Smooth transition for link color */
}

.nav-list a:hover {
  color: #3498db;
  /* Light blue on hover */
}</style>
