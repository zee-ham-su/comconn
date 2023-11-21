import { createRouter, createWebHistory } from 'vue-router';
import HelloWorld from '@/components/HelloWorld.vue';
import ResourcesPage from '@/components/ResourcesPage.vue';



const routes = [
    { path: '/', component: HelloWorld },
    { path: '/resources', component: ResourcesPage },
    // Add more routes as needed
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});
export default router;
