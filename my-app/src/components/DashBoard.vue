<template>
  <div class="dashboard-container">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/lux/bootstrap.min.css" integrity="sha384-9+PGKSqjRdkeAU7Eu4nkJU8RFaH8ace8HGXnkiKMP9I9Te0GJ4/km3L1Z8tXigpG" crossorigin="anonymous">
    <h2>Welcome to our Dashboard!</h2>
     <DashboardNavbar />
     <router-view/>

    <form @submit.prevent="logout">
      <button type="submit" class="logout-btn">Logout</button>
    </form>
  </div>
</template>

<script>
import apiClient from '@/services/api.js';
import DashboardNavbar from '@/components/DashboardNavbar.vue';

export default {
  components: {
    DashboardNavbar,
  },
  methods: {
    async logout() {
      try {
        // Make a request to your logout endpoint
        const response = await apiClient.delete('/logout');

        // Handle successful logout
        console.log('Logout successful:', response.data.message);

        // You can also navigate to the login page or perform other actions
        this.$router.push('/login');
      } catch (error) {
        // Handle logout error
        console.error('Logout failed:', error.response.data.message);
      }
    }
  }
}
</script>

<style scoped>
.dashboard-container {
  max-inline-size: 800px;
  margin: 20px auto;
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h2 {
  color: #333;
}

.logout-btn {
  background-color: #d9534f;
  color: #fff;
  border: none;
  padding: 10px 15px;
  border-radius: 5px;
  cursor: pointer;
  margin: 20px;
}
</style>
