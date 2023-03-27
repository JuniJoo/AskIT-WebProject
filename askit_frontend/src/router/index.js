import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import QuestionView from '@/views/QuestionView.vue'
import AskView from '@/views/AskView.vue'
import AboutView from "@/views/AboutView.vue";
import ModuleView from "@/views/ModuleView.vue";
import PrivacyView from "@/views/PrivacyView.vue";
import createdModule from "@/views/CreateModule.vue";
import CreateModule from "@/views/CreateModule.vue";
import LoginView from "@/views/LoginView.vue";
import SignUpView from "@/views/SignUpView.vue";
import SearchView from "@/views/SearchView.vue";
import AdvancedSearchView from "@/views/AdvancedSearchView.vue";

const routes = [
    {
        path: '/about',
        name: 'about',
        component: AboutView
    },
    {
        path: '/privacy',
        name: 'privacy',
        component: PrivacyView
    },
    {
        path: '/question/:id',
        name: 'question',
        component: QuestionView,
    },
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/ask/:mod',
        name: 'ask',
        component: AskView
    },
    {
        path: '/module/:mod',
        name: 'module',
        component: ModuleView
    },
    {
        path: '/log-in',
        name: 'LogIn',
        component: LoginView
    },
    {
        path: '/sign-up',
        name: 'SignUp',
        component: SignUpView
    },
    {
        path: '/search/',
        name: 'search',
        component: SearchView
    },
    {
        path: '/advanced-search/',
        name: 'advanced-search',
        component: AdvancedSearchView
    },
    {
        path: '/new',
        name: 'newmodule',
        component: CreateModule
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
