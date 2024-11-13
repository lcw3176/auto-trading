import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/store/auth';

const routes = [
  {
    path: '/',
    redirect: "/home"
  },

  {
    path: '/home',
    name: 'home',
    component: () => import(/* webpackChunkName: "home" */ '../views/HomeView.vue')
  },


  
  {
    path: '/:pathMatch(.*)*',
    redirect: '/404'
  },

  {
    path: '/404',
    name: 'notFound',
    component: () => import(/* webpackChunkName: "notFound" */ '../views/NotFoundView.vue')
  },

  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})


router.beforeEach((to, from, next) => {

  if ((to.path !== "/login" && to.path !== "/home") && isEmpty(useAuthStore().token)) {
      next("/login");
  } else if(to.path === "/login" && !isEmpty(useAuthStore().token)) {
      next("/home");
  } else {
      next();
  }
});

function isEmpty(input) {
  return typeof input === "undefined" ||
      input === null ||
      input === "" ||
      input === "null" ||
      input.length === 0 ||
      (typeof input === "object" && !Object.keys(input).length);
}

export default router