<template>
  <div>
    <h1>Community Resources</h1>
    <ul>
      <li v-for="resource in resources" :key="resource.id">
        {{ resource.name }} - {{ resource.description }}
      </li>
    </ul>
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
h1 {
  color: #42b983;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-block-end: 10px;
}
</style>
