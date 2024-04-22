<template>
  <div class="operation-container">
    <ul class="operation-list">
      <HistoryItem
        v-for="(data, index) in operationData"
        :key="index"
        :operationData="data"
      />
    </ul>
  </div>
</template>

<script>
import HistoryItem from "@/components/HistoryItem.vue";

export default {
  name: "HistoryList",
  components: {
    HistoryItem,
  },
  props: {
    operationData: {
      type: Array,
      required: true,
    },
  },
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
  padding-top: 20px;
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

.operation-container {
  padding: 20px;
}
</style>
