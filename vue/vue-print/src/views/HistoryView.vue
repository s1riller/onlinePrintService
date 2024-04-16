<template>
  <div class="container">
    <div class="history">
      <h2 class="title">История операций за</h2>
      <v-select v-model="currentMoth" :items="months"></v-select>
      <div>
        <template v-for="(progress, index) in progressBars" :key="index">
          <v-progress-linear
            :bg-color="progress.bgColor"
            :color="progress.color"
            :model-value="progress.value"
          ></v-progress-linear>
          <br />
        </template>
      </div>
    </div>
    <HistoryList :operationData="this.operationData" />
    <!-- Использование компонента HistoryList -->
  </div>
</template>

<script>
import HistoryList from "@/components/HistoryList.vue";
export default {
  components: {
    HistoryList, // Регистрация компонента внутри компонента HistoryView.vue
  },
  data() {
    return {
      currentMoth: null,
      months: [
        "Январь",
        "Февраль",
        "Март",
        "Апрель",
        "Май",
        "Июнь",
        "Июль",
        "Август",
        "Сентябрь",
        "Октябрь",
        "Ноябрь",
        "Декабрь",
      ],

      progressBars: [
        {
          bgColor: "red-darken-1",
          color: "red-darken-1",
          value: 15,
          name: "PDF",
          icon: "pdf",
        },
        {
          bgColor: "blue-darken-2",
          color: "blue-darken-2",
          value: 30,
          name: "docx",
          icon: "docx",
        },
        {
          bgColor: "green",
          color: "green",
          value: 45,
          name: "xls",
          icon: "xls",
        },
      ],

      operationData: [
        {
          name: "Дипломная работа 2021",
          date: {
            minute: 30,
            hour: 12,
            day: 21,
            month: "марта",
            year: 2024,
          },
          price: "$50.00",
          status: "Успешно",
        },
        {
          name: "Работа по проекту номваываер один",
          date: {
            minute: 45,
            hour: 14,
            day: 22,
            month: "апреля",
            year: 2024,
          },
          price: "$100.00",
          status: "В ожидании",
        },
      ],
    };
  },
  mounted() {
    this.currentMoth = this.months[new Date().getMonth()];
  },

  methods: {},
};
</script>

<style>
.history {
  border-radius: 10px;
  padding: 20px;
}

.title {
  font-size: 1.8rem;
  margin-bottom: 20px;
}

.operation-list {
  list-style: none;
  padding: 0;
}

.operation-item {
  display: flex;
  justify-content: space-between;
  border-bottom: 1px solid #ccc;
  padding: 10px 0;
}

.operation-info {
  flex: 1;
}

.operation-type {
  font-weight: bold;
  margin-bottom: 5px;
}

.operation-date {
  color: #666;
}

.operation-amount {
  font-weight: bold;
  color: #333;
}
</style>
