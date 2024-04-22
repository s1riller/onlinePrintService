<template>
  <v-app>
    <v-main>
      <router-view />
    </v-main>
    <BottomNavigation />
    <!-- Перемещаем компонент внутрь основного контента -->
  </v-app>
</template>

<script>
import BottomNavigation from './components/BottomNavigation.vue'

export default {
  name: 'App',

  components: {
    BottomNavigation,
  },

  data: () => ({
    //
  }),

  computed: {
    env() {
      return process.env
    },
  },
}
</script>
