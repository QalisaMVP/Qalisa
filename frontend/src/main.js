import { createApp } from 'NavBar.vue'
import App from './App.vue'
import { createRouter, createWebHashHistory } from 'vue-router';
import HomePage from './components/HomePage.vue';
import LearnPage from './components/LearnPage.vue';
import YourProfile from './components/YourProfile.vue';

const app = createApp(App);

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    { path: '/HomePage', component: HomePage },
    { path: '/LearnPage', component: LearnPage },
    { path: '/YourProfile', component: YourProfile }
  ]
});

app.use(router);

app.mount('#app');

vue.config.productionTip = false;
  
  
createApp(App).mount('#app')

