<template>
  <div>
    <div class="container">
      <h1>Community Reviews</h1>
        <div class="review-card" v-for="review in reviews" :key="review.id">
        <h2>User ID: {{ review.user_id }}</h2>
          <p>Resource ID: {{ review.resource_id }}</p>
          <p>Rating: {{ review.rating }}</p>
          <p>Comment: {{ review.comment }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import apiClient from '@/services/api.js';

export default {
  name: 'ReviewsPage',
 
  data() {
    return {
      reviews: [],
    };
  },
  mounted() {
    this.fetchReviews();
  },
  methods: {
    async fetchReviews() {
      try {
        const response = await apiClient.get('/reviews');
        this.reviews = response.data.reviews;
      } catch (error) {
        console.error('Error fetching reviews:', error);
      }
    },
  },
};
</script>

<style scoped>
/* Add styling for your ResourcesPage */
.container {
  max-inline-size: 800px;
  margin: 0 auto;
}

.review-card {
  background-color: #ffffff;
  border: 1px solid #3b1397;
  padding: 20px;
  margin-block-end: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h1 {
  color: #5842b9;
}
</style>