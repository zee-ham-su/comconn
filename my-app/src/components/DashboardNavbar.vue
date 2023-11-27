<template>
  <nav class="dashboard-navbar">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/lux/bootstrap.min.css" integrity="sha384-9+PGKSqjRdkeAU7Eu4nkJU8RFaH8ace8HGXnkiKMP9I9Te0GJ4/km3L1Z8tXigpG" crossorigin="anonymous">
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