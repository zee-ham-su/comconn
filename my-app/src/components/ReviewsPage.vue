<template>
  <div>
    <div class="container">
      <h1 class="title">Community Reviews</h1>

      <!-- Review Submission Form -->
      <form class="review-form" @submit.prevent="submitReview">
        <div class="form-group">
          <label for="user-id">User ID:</label>
          <input type="text" id="user-id" v-model="newReview.user_id" required>
        </div>

        <div class="form-group">
          <label for="resource-id">Resource ID:</label>
          <input type="text" id="resource-id" v-model="newReview.resource_id" required>
        </div>

        <div class="form-group">
          <label for="rating">Rating:</label>
          <input type="number" id="rating" v-model="newReview.rating" required>
        </div>

        <div class="form-group">
          <label for="comment">Comment:</label>
          <textarea id="comment" v-model="newReview.comment" required></textarea>
        </div>

        <button type="submit">Submit Review</button>
      </form>

      <!-- Display Reviews -->
      <div class="reviews-container">
        <div class="review-card" v-for="review in reviews" :key="review.id">
        <h2 class="user-id">User ID: {{ review.user_id }}</h2>
        <p class="resource-id">Resource ID: {{ review.resource_id }}</p>
        <p class="rating">Rating: {{ review.rating }}</p>
        <p class="comment">Comment: {{ review.comment }}</p>
      </div>
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
      newReview: {
        user_id: '',
        resource_id: '',
        rating: null,
        comment: '',
      },
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

    async submitReview() {
      try {
        // Make a POST request to submit a new review
        await apiClient.post('/reviews', this.newReview);

        // Clear the form and fetch the updated list of reviews
        this.newReview = {
          user_id: '',
          resource_id: '',
          rating: null,
          comment: '',
        };
        this.fetchReviews();
      } catch (error) {
        console.error('Error submitting review:', error);
      }
    },
  },
};
</script>

<style scoped>
/* Updated styling for your ReviewsPage */

.container {
  max-inline-size: 300px;
  margin: 0 auto;
}

.title {
  color: #5842b9;
  text-align: center;
  margin-block-end: 20px;
}

.review-form {
  background-color: rgb(25, 175, 70);
  border: 5px solid #ced4da;
  padding: 40px;
  border-radius: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin-block-end: 20px;
  position: absolute;
  inset-block-start: 120px;
  inset-inline-end: 40px;
}

.reviews-container {
  float: inline-end;
  max-inline-size: 500px;
}



.form-group {
  margin-block-end: 15px;
}

label {
  display: block;
  font-weight: bold;
  margin-block-end: 5px;
}

input,
textarea {
  inline-size: 100%;
  padding: 10px;
  border: 1px solid #ced4da;
  border-radius: 4px;
  box-sizing: border-box;
  font-size: 1em;
  margin-block-end: 10px;
}

button {
  background-color: #08804e;
  color: #ffffff;
  padding: 10px 15px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1.2em;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: rgb(14, 192, 88);
}

.review-card {
  background-color: #ffffff;
  border: 1px solid #3b1397;
  padding: 20px;
  margin-block-end: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-inline-size: 150%; /* Adjust the width as needed */
  margin-inline-start: 0;
}

.user-id,
.resource-id,
.rating,
.comment {
  color: #2c3e50;
  font-size: 1.2em;
  margin-block-end: 10px;
}

</style>
