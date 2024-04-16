<template>
  <v-bottom-navigation :elevation="24">
    <v-btn value="recent" @click="$router.push('/operation-history')">
      <v-icon>mdi-history</v-icon>
      <span>История</span>
    </v-btn>

    <v-btn value="favorites" @click="$router.push('/document-choice')">
      <v-icon>mdi-printer</v-icon>
      <span>Печать</span>
    </v-btn>

    <v-btn value="nearby" @click="$router.push({ name: 'user-profile' })">
      <v-icon>mdi-account</v-icon>
      <span>Профиль</span>
    </v-btn>

    <v-btn value="nearby" color="primary" @click="$router.push('/auth')">
      <v-icon color="primary">mdi-login</v-icon>
      <span color="primary">Войти</span>
    </v-btn>
  </v-bottom-navigation>
</template>
