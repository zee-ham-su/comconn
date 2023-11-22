<!-- UserProfile.vue -->
<template>
    <div>
        <div class="container">
            <h1>Community Users</h1>
            <div class="user-card" v-for="user in users" :key="user.id">
                <h2>User ID: {{ user.id }}</h2>
                <p>Username: {{ user.username }}</p>
                <p>Email: {{ user.email }}</p>
                <!-- Add more details as needed -->
            </div>
        </div>
    </div>
</template>

<script>
import apiClient from '@/services/api.js';

export default {
    name: 'UserProfile',
    data() {
        return {
            users: [],
        };
    },
    mounted() {
        this.fetchUserData();
    },
    methods: {
        async fetchUserData() {
            try {
                const response = await apiClient.get('/users'); // Adjust the API endpoint
                this.users = response.data.users; // Assuming your API returns an array of users
            } catch (error) {
                console.error('Error fetching user data:', error);
            }
        },
    },
};
</script>

<style scoped>
/* Add styling for your UserProfile */
.container {
    max-inline-size: 800px;
    margin: 0 auto;
}

/* Add more styling as needed */
.user-card {
    background-color: #ffffff;
    border: 1px solid #1d6e4c;
    padding: 20px;
    margin-block-end: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h1 {
    color: #5842b9;
}
</style>
