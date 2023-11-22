import axios from 'axios';

const apiClient = axios.create({
    baseURL: 'http://localhost:5000',  // Replace with your backend API base URL
    headers: {
        'Content-Type': 'application/json',
        // Add any headers you need, such as authentication tokens
    },
});

export default apiClient;
