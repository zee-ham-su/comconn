import { createRouter, createWebHistory } from 'vue-router';
import HelloWorld from '@/components/HelloWorld.vue';
import ResourcesPage from '@/components/ResourcesPage.vue';
import ReviewsPage from '@/components/ReviewsPage.vue';
import UserProfile from '@/components/UserProfile.vue';
import LoginForm from '@/components/LoginForm.vue';
import DashBoard from '@/components/DashBoard.vue';
import('@/update_profile.js');
import('@/login.js');
import('@/registerForm.js');


const routes = [
    { path: '/', component: HelloWorld },
    { path: '/resources', component: ResourcesPage},
    { path: '/reviews', component: ReviewsPage},
    { path: '/user', component: UserProfile},
    { path: '/login', component: LoginForm},
    { path: '/dashboard', component: DashBoard},
    
    // Add more routes as needed
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});
export default router;
