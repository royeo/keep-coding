import Vue from 'vue'
import Router from 'vue-router'
import index from '../page/index.vue'
import content from '../page/content.vue'
import Frame from '../frame/subroute.vue'
import userIndex from '../page/user/index.vue'
import userInfo from '../page/user/info.vue'
import userLove from '../page/user/love.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    },
    {
      path: '/content',
      name: 'content',
      component: content
    },
    {
      path: '/user',
      component: Frame,
      children: [
        {path: '/', component: userIndex},
        {path: 'info', component: userInfo},
        {path: 'love', component: userLove}
      ]
    }
  ]
})
