import Vue from 'vue';

import Sidebar from './components/app/Sidebar.vue'
import App from './App.vue'

Vue.component('app-sidebar', Sidebar)

let app = document.getElementById('app')
new Vue({
    el: "#app",
})