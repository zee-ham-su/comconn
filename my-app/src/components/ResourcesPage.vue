<template>
  <div>
    <div class="container">
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/lux/bootstrap.min.css" integrity="sha384-9+PGKSqjRdkeAU7Eu4nkJU8RFaH8ace8HGXnkiKMP9I9Te0GJ4/km3L1Z8tXigpG" crossorigin="anonymous">
      <h1 class="title">Community Resources</h1>
      <div class="resource-card" v-for="resource in resources" :key="resource.id">
        <h2 class="resource-title">{{ resource.name }}</h2>
        <p class="resource-description">{{ resource.description }}</p>
      </div>
    </div>
    <div id="map" class="map-container"></div>
  </div>
</template>

<script>
/* global google */
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
    this.loadGoogleMapsScript();
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

    loadGoogleMapsScript() {
      const script = document.createElement('script');
      script.src = `https://maps.googleapis.com/maps/api/js?key=AIzaSyCqoeDgkfk_2-3csLzYkPcu9JU5iOSN_Uk
&callback=initMap`;
      script.async = true;
      script.defer = true;
      document.head.appendChild(script);
      script.onload = () => {
        this.initMap();
      };
    },

    initMap() {
      // Map initialization logic
      const map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 5.6037, lng: -0.1870 }, // Centered around Accra, Ghana
        zoom: 8, // Adjust the zoom level as needed
      });

      // Add markers for each resource
      this.resources.forEach(resource => {
        new google.maps.Marker({
          position: { lat: resource.latitude, lng: resource.longitude },
          map,
          title: resource.name,
        });
      });
    },
  },
};
</script>

<style scoped>
/* Your existing styling */
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
  font-size: 1.5em;
  margin-block-end: 10px;
}

.resource-description {
  color: #0c0e0d;
  font-size: 1.2em;
}

/* Adjusted styling for the map */
.map-container {
  block-size: 300px;
  margin-block-start: 20px;
}
</style>
