// src/login.js

import { createApp } from 'vue';
import api from '@/services/api';

const app = createApp({});

app.component('LoginForm', {
    
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

