<template>
  <nav class="navbar">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/lux/bootstrap.min.css" integrity="sha384-9+PGKSqjRdkeAU7Eu4nkJU8RFaH8ace8HGXnkiKMP9I9Te0GJ4/km3L1Z8tXigpG" crossorigin="anonymous">
    <ul class="nav-list">
      <li><router-link to="/">Home</router-link></li>
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
