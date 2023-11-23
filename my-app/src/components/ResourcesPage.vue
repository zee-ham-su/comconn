<template>
  <div class="container">
    <h1 class="title">Community Resources</h1>
    <div class="resource-card" v-for="resource in resources" :key="resource.id">
      <h2 class="resource-title">{{ resource.name }}</h2>
      <p class="resource-description">{{ resource.description }}</p>
    </div>
  </div>
</template>

<script>
import apiClient from '@/services/api.js';

export default {
  name: 'ResourcesPage',

  data() {
    return {
      resources: [],
    };
  },
  mounted() {
    this.fetchResources();
  },
  methods: {
    async fetchResources() {
      try {
        const response = await apiClient.get('/resources');
        this.resources = response.data.resources;
      } catch (error) {
        console.error('Error fetching resources:', error);
      }
    },
  },
};
</script>

<style scoped>
/* Updated styling for your ResourcesPage */
.container {
  max-inline-size: 800px;
  margin: 0 auto;
}

.title {
  color: #5842b9;
  text-align: center;
  margin-block-end: 20px;
}

.resource-card {
  background-color: #ffffff;
  border: 1px solid #1d6e4c;
  padding: 20px;
  margin-block-end: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.resource-title {
  color: #2c3e50;
  /* Dark blue-gray */
  font-size: 1.5em;
  margin-block-end: 10px;
}

.resource-description {
  color: #0c0e0d;
  /* Gray */
  font-size: 1.2em;
}
</style>
