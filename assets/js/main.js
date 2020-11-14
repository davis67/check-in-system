import Vue from 'vue';
import App from './App.vue'
let app = document.getElementById('app')

Vue.component('load-app-you', App)

new Vue({
    el: "#app",
})