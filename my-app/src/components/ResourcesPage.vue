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
export default {
  name: 'ResourcesPage',
  data() {
    return {
      resources: [
        { id: 1, name: 'Resource 1', description: 'Description 1' },
        { id: 2, name: 'Resource 2', description: 'Description 2' },
        // Add more sample resources or fetch them from your API
      ],
    };
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
