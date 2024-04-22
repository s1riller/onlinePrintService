import { createStore } from 'vuex'
import userModule from './user';
import dialogWindow from './dialogWindow.js';
export default createStore({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    user: userModule,
    dialogWindow: dialogWindow
  }
})
