<template>
  <div class="login-form-container">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/lux/bootstrap.min.css" integrity="sha384-9+PGKSqjRdkeAU7Eu4nkJU8RFaH8ace8HGXnkiKMP9I9Te0GJ4/km3L1Z8tXigpG" crossorigin="anonymous">
    <h2>Login</h2>
    <form @submit.prevent="login" class="login-form">
      <label for="username">Username:</label>
      <input type="text" id="username" v-model="username" required>

      <label for="password">Password:</label>
      <input type="password" id="password" v-model="password" required>

      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
import apiClient from '@/services/api.js';
export default {
name: 'LoginForm',
data() {
  return {
    username: '',
    password: '',
  };
},
methods: {
        async login() {
    try {
      // Use the API service to send a login request
      const response = await apiClient.post('/login', {
        username: this.username,
        password: this.password,
      });
        // Check if the login was successful
        if (response.status === 200) {
          // Redirect to the dashboard
          this.$router.push('/dashboard');
        } else {
          // Handle other response statuses if needed
          if (response.data) {
            console.error('Login failed:', response.data.message);
          } else {
            console.error('Login failed. No response data available.');
          }
        }
      } catch (error) {
        // Handle errors
        console.error('Login failed:', error.response ? error.response.data.message : 'Unknown error');
      }
    },
},
};
</script>

<style scoped>
.login-form-container {
  max-inline-size: 300px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  background-color: #fff;
  text-align: center;
  margin-top: 30px;
}

h2 {
  color: #333;
}

.login-form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

label {
  margin-block-end: 8px;
  color: #555;
}

input {
  inline-size: 100%;
  padding: 10px;
  margin-block-end: 15px;
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 3px;
}

button {
  background-color: #4caf50;
  color: white;
  padding: 12px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}
</style>
