<template>
  <div>
    <div class="container">
      <h1>Community Reviews</h1>
      <div class="review-card" v-for="review in reviews" :key="review.id">
        <h2>{{ review.title }}</h2>
        <p>{{ review.content }}</p>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'ReviewsPage',
 
  data() {
    return {
      reviews: [
        { id: 1, title: 'Review 1', content: 'Content 1' },
        { id: 2, title: 'Review 2', content: 'Content 2' },
        // Add more sample reviews or fetch them from your API
      ],
    };
  },
};
</script>

<style scoped>
/* Add styling for your ReviewsPage */
.container {
  max-inline-size: 800px;
  margin: 0 auto;
}

.review-card {
  background-color: #ffffff;
  border: 1px solid #e1e1e1;
  padding: 20px;
  margin-block-end: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h1 {
  color: #42b983;
}
</style>
