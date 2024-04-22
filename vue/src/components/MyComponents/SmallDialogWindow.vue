<template>
  <div class="pa-4 text-center">
    <v-dialog v-model="internalDialog" max-width="500" persistent>
      <v-list class="py-2" color="primary" elevation="20" rounded="lg">
        <v-list-item>
          <v-list-item-icon>
            <v-icon>mdi-information-outline</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <!-- <v-list-item-title v-text="title"></v-list-item-title> -->
            <p>{{ text }}</p>
          </v-list-item-content>
          <v-list-item-action>
            <v-btn icon @click="closeDialog">
              <v-icon>mdi-close-circle-outline</v-icon>
            </v-btn>
          </v-list-item-action>
        </v-list-item>
      </v-list>
    </v-dialog>
  </div>
</template>

<script>
export default {
  name: 'SmallDialogWindowNotification',

  props: {
    dialog: {
      type: Boolean,
      default: false,
    },
    title: {
      type: String,
      default: 'Default Title',
    },
    text: {
      type: String,
      default: 'Default text content.',
    },
  },

  data() {
    return {
      internalDialog: this.dialog, // Инициализируем внутреннее состояние значениями пропа
    }
  },

  watch: {
    // Отслеживаем изменения пропа dialog
    dialog(newValue) {
      this.internalDialog = newValue
    },
    // Отслеживаем изменения внутреннего состояния для информирования родителя
    internalDialog(newValue) {
      this.$emit('update:dialog', newValue)
    },
  },

  mounted() {
    setTimeout(() => {
      this.closeDialog()
    }, 1000)
  },
  methods: {
    closeDialog() {
      this.internalDialog = false
    },
  },
}
</script>

<style scoped>
p {
  padding-top: 10px;
  white-space: pre-wrap;
}
</style>
