export default {
  state: {
    dialogWindows: {
      loginDialog: false,
      signUpDialog: {
        state: false,
        data: null,
        time: null,
      },
      feedbackDialog: false,
    },
  },
  getters: {
    getDialogState: (state) => (dialogName) => {
      return state.dialogWindows[dialogName].state ?? state.dialogWindows[dialogName];
    },

    getDialogData: (state) => (dialogName) => {
      return state.dialogWindows[dialogName].data;
    }
  },
  mutations: {

    SET_DIALOG_STATE(state, { dialogName, status }) {
      if (typeof state.dialogWindows[dialogName] === 'object' && state.dialogWindows[dialogName] !== null) {
        state.dialogWindows[dialogName].state = status;
      } else {
        state.dialogWindows[dialogName] = status;
      }
    },

    SET_DIALOG_DATA(state, { dialogName, data }) {
      if (state.dialogWindows[dialogName] && typeof state.dialogWindows[dialogName] === 'object') {
        state.dialogWindows[dialogName].data = data;
      }
    },
  },
  actions: {
    updateDialogState({ commit }, { dialogName, status }) {
      commit('SET_DIALOG_STATE', { dialogName, status });
    },

    updateDialogData({ commit }, { dialogName, data }) {
      commit('SET_DIALOG_DATA', { dialogName, data });
    },
  }
};
