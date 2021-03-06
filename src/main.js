/*=========================================================================================
  File Name: main.js
  Description: main vue(js) file
  ----------------------------------------------------------------------------------------
  Item Name: Vuexy - Vuejs, HTML & Laravel Admin Dashboard Template
  Author: Pixinvent
  Author URL: http://www.themeforest.net/user/pixinvent
==========================================================================================*/


import Vue from 'vue'
import App from './App.vue'
// Vuesax Component Framework
import Vuesax from 'vuesax'
import 'material-icons/iconfont/material-icons.css' //Material Icons
import 'vuesax/dist/vuesax.css' // Vuesax
// axios
// Filters
import './filters/filters.js'
// Theme Configurations
import '../themeConfig.js'
// Globally Registered Components
import './globalComponents.js'
// Styles: SCSS
import './assets/scss/main.scss'
// Tailwind
import '@/assets/css/main.css'
// Vue Router
import router from './router'
// Vuex Store
import store from './store/store'
// Vue idle
// VeeValidate
import VeeValidate from 'vee-validate'
// Vuejs - Vue wrapper for hammerjs
import {VueHammer} from 'vue2-hammer'
// PrismJS
import 'prismjs'
import 'prismjs/themes/prism-tomorrow.css'
import "vue2-perfect-scrollbar/dist/vue2-perfect-scrollbar.css";

import PerfectScrollbar from 'vue2-perfect-scrollbar'
// mock
import './fake-db/index.js'
import {getAPI} from "./axios";

// fontawesome
import {library} from '@fortawesome/fontawesome-svg-core'
import {faApple, fab} from '@fortawesome/free-brands-svg-icons'
import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'
// import GmapVue from 'gmap-vue'

library.add(faApple, fab)

//fab

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.use(Vuesax)


Vue.prototype.$http = getAPI


Vue.use(VeeValidate)

Vue.use(PerfectScrollbar);


Vue.use(VueHammer)



// Feather font icon
require('./assets/css/iconfont.css')


// Vue select css
// Note: In latest version you have to add it separately
// import 'vue-select/dist/vue-select.css';


// sets up the idle time,i.e. time left to logout the user on no activity

let token = localStorage.getItem('access_token')
if (token) {
    getAPI.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('access_token')}`
}


Vue.config.productionTip = false

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')
