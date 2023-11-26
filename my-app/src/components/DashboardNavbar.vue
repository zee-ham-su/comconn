<template>
  <nav class="dashboard-navbar">
    <ul class="dashboard-nav-list">
      <li><router-link to="/resources">Resources</router-link></li>
      <li><router-link to="/reviews">Reviews</router-link></li>
      <li><router-link to="/user">User Profile</router-link></li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'DashboardNavbar',
};
</script>

<style scoped>
.dashboard-navbar {
  background-color: #2c3e50;
  /* Dark blue-gray */
  color: white;
  padding: 10px;
}

.dashboard-nav-list {
  list-style-type: none;
  margin: 0;
  padding: 0;
  display: flex;
}

.dashboard-nav-list li {
  margin-inline-end: 15px;
}

.dashboard-nav-list a {
  text-decoration: none;
  color: white;
  font-weight: bold;
  transition: color 0.3s ease;
}

.dashboard-nav-list a:hover {
  color: #3498db;
}
</style>
l