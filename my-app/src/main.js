import { createApp } from 'vue'
import App from './App.vue'

const app = createApp(App)
app.config.globalProperties.apiURL = 'http://localhost:5000/api'  // Update with your Flask API URL
app.mount('#app')
