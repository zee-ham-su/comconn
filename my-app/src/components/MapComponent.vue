<template>
    <div class="map-container">
        <gmp-map :center="mapCenter" :zoom="mapZoom" map-id="DEMO_MAP_ID"></gmp-map>
    </div>
</template>

<script>
/* global google */

export default {
    data() {
        return {
            mapCenter: { lat: 5.6037, lng: -0.1870 },
            mapZoom: 10,
            placesService: null,
        };
    },
    mounted() {
        // Load the Google Maps API script
        const script = document.createElement("script");
        script.src = `https://maps.googleapis.com/maps/api/js?key=AIzaSyB41DRUbKWJHPxaFjMAwdrzWzbVKartNGg&libraries=places&callback=initMap&v=beta`;
        script.defer = true;
        document.head.appendChild(script);

        // Define initMap globally
        window.initMap = () => {
            console.log("Maps JavaScript API loaded.");

            this.initializeMap(); // Call the function within the component
            this.initializePlacesService();
        };
    },
    methods: {
        initializeMap() {
            // Your map initialization code goes here
            console.log("Map initialized");
        },
        initializePlacesService() {
            // Initialize the Places Service for searching
            this.placesService = new google.maps.places.PlacesService(document.createElement("div"));
        },
        searchPlaces(query) {
            // Perform a search for places
            const request = {
                location: new google.maps.LatLng(...this.mapCenter.split(",")),
                radius: 5000, // Search within a radius of 5000 meters (adjust as needed)
                query: query,
            };

            this.placesService.textSearch(request, (results, status) => {
                if (status === google.maps.places.PlacesServiceStatus.OK) {
                    // Handle the results, e.g., add markers for each place
                    results.forEach((place) => {
                        this.addMarker(place.geometry.location, place.name);
                    });
                }
            });
        },
        addMarker(position, title) {
            // Add a marker to the map
            new google.maps.Marker({
                position: position,
                map: this.$refs.gmpMap.$mapObject, // Access the underlying Google Maps object
                title: title,
            });
        },
    },
};
</script>

<style scoped>
.map-container {
    display: flex;
    justify-content: flex-start;
    /* Align map to the left */
    margin: 20px;
    /* Add margin for spacing */
}

gmp-map {
    height: 400px;
    /* Set a specific height for the map */
    width: 70%;
    /* Adjust the width as needed */
}</style>
