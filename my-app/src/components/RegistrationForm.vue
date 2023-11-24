<template>
    <div class="container">
        <h1 class="title">Register</h1>
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
import apiClient from '@/services/api.js';

export default {
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
/* Styling for RegistrationForm */
.container {
    max-inline-size: 800px;
    margin: 0 auto;
}

.title {
    color: #5842b9;
    text-align: center;
    margin-block-end: 20px;
}

.registration-form {
    background-color: #ffffff;
    border: 1px solid #1d6e4c;
    padding: 20px;
    margin-block-end: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
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
</style>
