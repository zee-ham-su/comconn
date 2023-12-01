import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.css';

const app = createApp(App);

// Set the configuration for custom elements
app.config.compilerOptions.isCustomElement = (tag) => tag.startsWith('gmp-');

// Use the router and then mount the app
app.use(router).mount('#app');
