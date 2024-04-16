<template>
  <li class="operation-item">
    <div class="operation-info">
      <a href="#" class="social-icon">
        <i
          :class="typeFiles[0].icon"
          :style="{ color: typeFiles[0].color }"
        ></i>
      </a>
      <p class="operation-type">{{ truncateOperationName(operation.name) }}</p>
      <p class="operation-date">
        {{ operation.date.day }} {{ operation.date.month }}
        {{ operation.date.year }}, {{ operation.date.hour }}:{{
          operation.date.minute
        }}
      </p>
      <p
        class="operation-status"
        :style="{ color: getStatusColorByName(operation.status) }"
      >
        {{ operation.status }}
      </p>
      <div class="operation-info-icon">
        <i
          :class="getOperationStatusIcon(operation.status)"
          :style="{ color: getStatusColorByName(operation.status) }"
        ></i>
        <p class="operation-description">{{ operation.description }}</p>
      </div>
    </div>
    <p class="operation-amount">{{ operation.price }}</p>
  </li>
</template>

<script>
export default {
  props: {
    operationData: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      typeFiles: [
        { name: "PDF", icon: "fa-solid fa-file-pdf fa-lg", color: "#ff0000" },
        { name: "XLS", icon: "fa-solid fa-file-excel fa-lg", color: "#008000" },
        { name: "WORD", icon: "fa-solid fa-file-word fa-lg", color: "#0000FF" },
      ],
      statusColors: [
        { name: "Успешно", color: "#189e18" },
        { name: "В ожидании", color: "#b8981c" },
        { name: "Отменено", color: "#ff0000" },
        { name: "", color: "#000000" },
      ],
    };
  },
  computed: {
    operation() {
      return {
        ...this.operationData,
      };
    },
  },
  methods: {
    getStatusColorByName(statusName) {
      const foundStatus = this.statusColors.find(
        (status) => status.name === statusName
      );
      return foundStatus ? foundStatus.color : "#000000"; // Возвращаем черный цвет по умолчанию
    },
    truncateOperationName(name) {
      // Обрезаем название операции до 20 символов
      return name.length > 15 ? name.slice(0, 15) + "..." : name;
    },
    getOperationStatusIcon(statusName) {
      // Метод для получения иконки для статуса операции
      // Здесь вы можете возвращать различные иконки в зависимости от статуса операции
      // Например, используя библиотеку FontAwesome, вы можете вернуть разные иконки для разных статусов
      switch (statusName) {
        case "Успешно":
          return "fas fa-check-circle"; // Иконка для успешной операции
        case "В ожидании":
          return "fas fa-hourglass-half"; // Иконка для операции в ожидании
        case "Отменено":
          return "fas fa-times-circle"; // Иконка для отмененной операции
        default:
          return "fas fa-question-circle"; // Иконка по умолчанию для неопределенного статуса
      }
    },
  },
};
</script>

<style scoped>
.operation-info-icon {
  display: inline-block; /* Изменено с inline-block */
}
.operation-info-icon i {
  margin-right: 10px; /* Добавляет небольшой отступ между иконкой и описанием */
}

.operation-item {
  background-color: #cccbc8;
  margin-bottom: 10px;
  border-radius: 10px 10px 10px 10px;
  width: auto;
}

.operation-info {
  padding-left: 20px;
}
.operation-amount {
  padding-right: 20px;
  margin-top: 50px;
  font-size: 20px;
}

.operation-type {
  font-size: 24px;
}
</style>
