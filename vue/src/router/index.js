import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/auth',
    name: 'auth',
    component: () => import('@/views/LoginView.vue')
  },
  {
    path: '/operation-history',
    name: 'operation-history',
    component: () => import('@/views/HistoryView.vue')
  },
  {
    path: '/document-choice',
    name: 'document-choice',
    component: () => import('@/views/PrintPage.vue')
  },
  {
    path: '/profile',
    name: 'user-profile',
    component: () => import('@/views/ProfileView.vue')
  }

]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
