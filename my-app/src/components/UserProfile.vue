<!-- UserProfile.vue -->
<template>
    <div>
        <div class="container">
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/lux/bootstrap.min.css" integrity="sha384-9+PGKSqjRdkeAU7Eu4nkJU8RFaH8ace8HGXnkiKMP9I9Te0GJ4/km3L1Z8tXigpG" crossorigin="anonymous">
            <h1 class="title">Community Users</h1>
            <div class="user-card" v-for="user in users" :key="user.id">
                <p>Username: {{ user.username }}</p>
                <p>Email: {{ user.email }}</p>
                <!-- Add more details as needed -->
            </div>
        </div>
    </div>
</template>

<script>
import apiClient from '@/services/api.js';
import '@/update_profile.js';

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
.title{
    color: #5842b9;
    text-align: start;
    margin-block-end: 20px; 
}

/* Add more styling as needed */
.user-card {
    background-color: #ffffff;
    border: 1px solid #1d6e4c;
    padding: 20px;
    margin-block-end: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    position: left;
    max-inline-size: 60%;
}

h1 {
    color: #5842b9;
    position: left;
}
</style>
