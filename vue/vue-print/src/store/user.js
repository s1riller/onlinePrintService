// user.js
export default {
  state: {
    firstName: null,
    lastName: null
  },
  getters: {
    fullName(state) {
      return `${state.firstName} ${state.lastName}`;
    }
  },
  mutations: {
    setFirstName(state, firstName) {
      state.firstName = firstName;
    },
    setLastName(state, lastName) {
      state.lastName = lastName;
    }
  },
  actions: {
    updateFirstName({ commit }, firstName) {
      commit('setFirstName', firstName);
    },
    updateLastName({ commit }, lastName) {
      commit('setLastName', lastName);
    }
  }
};
