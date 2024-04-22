<template>
  <div>
    <v-btn @click="scanDocument">
      <span>Сканировать документ</span>
    </v-btn>
  </div>
  <div>
    <v-btn @click="chooseDocument">
      <span>Выбрать документ{{ djangoUrl }}</span>
    </v-btn>
  </div>
  <div>
    <input type="file" @change="uploadDocument" />
    <span>Загрузить документ </span>
  </div>
</template>

<script>
export default {
  data() {
    return {
      djangoUrl: process.env.DJANGO_URL,
    };
  },
};
</script>
