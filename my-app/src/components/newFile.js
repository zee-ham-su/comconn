import apiClient from '@/services/api.js';

export default (await import('vue')).defineComponent({
name: 'LandingPage',
data() {
return {
formData: {
username: '',
email: '',
password: '',
},
};
},

mounted() {
this.loadGoogleMapsScript();
},

methods: {
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
center: { lat: 37.7749, lng: -122.4194 },
zoom: 12, // Default zoom level
});
},
methods: {
async register() {
try {
const response = await apiClient.post('/register', this.formData);
console.log('Registration successful:', response.data.message);
} catch (error) {
console.error('Error during registration:', error);
}
},
},
}
});
