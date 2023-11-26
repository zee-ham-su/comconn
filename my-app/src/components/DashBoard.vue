<template>
  <div class="dashboard-container">
    <h2>Welcome to your Dashboard!</h2>
     <DashboardNavbar />
     <router-view/>

    <form action="/logout" method="post">
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
        const response = await apiClient.post('/logout');

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
