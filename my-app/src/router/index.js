import { createRouter, createWebHistory } from 'vue-router';
import HelloWorld from '@/components/HelloWorld.vue';
import ResourcesPage from '@/components/ResourcesPage.vue';
import ReviewsPage from '@/components/ReviewsPage.vue';


const routes = [
    { path: '/', component: HelloWorld },
    { path: '/resources', component: ResourcesPage },
    { path: '/reviews', component: ReviewsPage},
    // Add more routes as needed
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});
export default router;
