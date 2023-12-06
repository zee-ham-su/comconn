<template>
  <div>
     <NavigationBar />
     <img src="@/assets/map-regular-24.png" alt="My Website Logo" />
     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/lux/bootstrap.min.css" integrity="sha384-9+PGKSqjRdkeAU7Eu4nkJU8RFaH8ace8HGXnkiKMP9I9Te0GJ4/km3L1Z8tXigpG" crossorigin="anonymous">
    <h1>Welcome to CommunityConnect</h1>
    <p>Tackling restricted access to accurate and up-to-date information about critical community resources.</p>
  </div>
  <div>
    <img src="../assets/background_img.png" alt="background img" class="img1">
  </div>
  <div class="text1">
    <p>Having access to critical community resources and 
      facilities is very important for a easy and smooth life. 
      Below are some features explained to help you know how to 
      utilize the platform to access the critical community resources and facilities. </p>
  </div>
    <MapComponent />
  <div class="feature2">
    <img src="../assets/feature2_img.png" alt="feature img" class="img3">
    <div class="text-box2">
    <h2>Community Reviews</h2>
    <p>With the help of the reviews left by other users about the critical resources in your commmunity, 
      you are going to be up-to-date with about the critical resources so you are not left stranded. 
      You can also add you reviews to help and also help improve the facilities you visited</p>
    </div>
  </div>
  <div class="container">
    <h1 class="title">Sign Up</h1>
    <form @submit.prevent="register" class="registration-form">
      <div class="form-group">
        <label for="username" class="form-label">Username:</label>
        <input type="text" id="username" v-model="formData.username" class="form-input" required />
      </div>

      <div class="form-group">
        <label for="email" class="form-label">Email:</label>
        <input type="email" id="email" v-model="formData.email" class="form-input" required />
      </div>

      <div class="form-group">
        <label for="password" class="form-label">Password:</label>
        <input type="password" id="password" v-model="formData.password" class="form-input" required />
      </div>

      <div class="form-group">
        <button type="submit" class="form-button">Register</button>
      </div>
    </form>
  </div>
</template>

<script>
import NavigationBar from '@/components/NavigationBar.vue';
import apiClient from '@/services/api.js';
import MapComponent from "@/components/MapComponent.vue";

export default {
  name: 'HelloWorld',
  components: {
    NavigationBar,
    MapComponent,
  },
  data() {
    return {
      formData: {
        username: '',
        email: '',
        password: '',
      },
    };
  },

  
  methods: {
    async register() {
      try {
        const response = await apiClient.post('/register', this.formData);
        console.log('Registration successful:', response.data.message);
      } catch (error) {
        console.error('Error during registration:', error);
      }
    },
  },
};
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #019251;
}

.container {
  max-inline-size: 800px;
  margin: 0 auto;
}

.title {
  color: #5842b9;
  position: absolute;
  inset-block-start: 60px;
  inset-inline-end: 150px;
}

.registration-form {
  background-color: #ffffff;
  border: 1px solid #5b1d6e;
  padding: 20px;
  margin-block-end: 20px;
  border-radius: 16px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  position: absolute;
  inset-block-start: 120px;
  inset-inline-end: 40px;
}

.form-group {
  margin-block-end: 20px;
}

.form-label {
  color: #2c3e50;
  /* Dark blue-gray */
  font-size: 1.2em;
  margin-block-end: 10px;
}

.form-input {
  inline-size: 100%;
  padding: 8px;
  font-size: 1em;
  border: 1px solid #bdc3c7;
  border-radius: 4px;
}

.form-button {
  background-color: #3498db;
  color: #ffffff;
  padding: 10px 15px;
  font-size: 1.2em;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
gmp-map {
  height: 400px;
}
.img1{
  display: flex;
  justify-content: flex-start;
  width: 100%;
}
.img3{
  /*display: flex;
  position: relative;
  right: auto;*/
  float: right;
  width: 54%;
  margin: 20px;
}
.text-box2{
    margin-left: 20px;
    padding: 20px;
  }
.text1{
  text-align: center;
  padding-top: 30px;
}
</style>
