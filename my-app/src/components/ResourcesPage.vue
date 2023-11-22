<template>
  <div class="container">
    <h1>Community Resources</h1>
    <div class="resource-card" v-for="resource in resources" :key="resource.id">
      <h2>{{ resource.name }}</h2>
      <p>{{ resource.description }}</p>
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
/* Add styling for your ResourcesPage */
.container {
  max-inline-size: 800px;
  margin: 0 auto;
}

.resource-card {
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