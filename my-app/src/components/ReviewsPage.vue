<template>
  <div>
    <div class="container">
      <h1 class="title">Community Reviews</h1>
      <div class="review-card" v-for="review in reviews" :key="review.id">
        <h2 class="user-id">User ID: {{ review.user_id }}</h2>
        <p class="resource-id">Resource ID: {{ review.resource_id }}</p>
        <p class="rating">Rating: {{ review.rating }}</p>
        <p class="comment">Comment: {{ review.comment }}</p>
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
/* Updated styling for your ReviewsPage */
.container {
  max-inline-size: 800px;
  margin: 0 auto;
}

.title {
  color: #5842b9;
  text-align: center;
  margin-block-end: 20px;
}

.review-card {
  background-color: #ffffff;
  border: 1px solid #3b1397;
  padding: 20px;
  margin-block-end: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.user-id,
.resource-id,
.rating,
.comment {
  color: #2c3e50;
  /* Dark blue-gray */
  font-size: 1.2em;
  margin-block-end: 10px;
}</style>
