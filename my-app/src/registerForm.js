
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