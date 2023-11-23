// src/login.js

import { createApp } from 'vue';
import api from '@/services/api';

const app = createApp({});

app.component('LoginForm', {
    template: `
    <div>
      <h2>Login</h2>
      <p>LoginForm is loaded!</p>
      <form @submit.prevent="login">
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="username" required><br>

        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required><br>

        <button type="submit">Login</button>
      </form>
    </div>
  `,
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
                const response = await api.post('/login', {
                    username: this.username,
                    password: this.password,
                });

                // Handle the response as needed (e.g., show a success message)
                console.log(response.data.message);
            } catch (error) {
                // Handle errors (e.g., show an error message)
                console.error('Login failed:', error.response.data.message);
            }
        },
    },
});

