<template>
  <div class="container">
    <div class="profile">
      <div class="user-image-full-name">
        <img
          src="https://sun9-78.userapi.com/impg/RyaZqHaI0PoBop71gUpl_es0Xoeq4cGi494hPw/iSZPSkuZsJQ.jpg?size=1016x1019&quality=95&sign=0cf18e0f26ca8ade841468459e9e0044&type=album"
          alt="User Avatar"
          class="avatar"
        />
        <h1 class="username">John Doe</h1>

        <NotificationBell class="bell" :amountNews="10" />
      </div>

      <div class="user-details">
        <div class="numberSheetsPrinted">
          <span class="user-details-span">Распечатано</span>
          <span class="user-details-span-detail">100</span>
        </div>
        <div class="amountMoneySpent">
          <span class="user-details-span">Потрачено</span>
          <span class="user-details-span-detail">100Р</span>
        </div>
      </div>
      <p class="bio">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae urna
        eget nunc hendrerit tristique eu ac odio.
      </p>
    </div>
  </div>
</template>

<script>
import NotificationBellComponent from "@/components/MyComponents/NotificationBellComponent.vue";

export default {
  name: "UserProfile", // Используем имя компонента "UserProfile"
  components: {
    NotificationBell: NotificationBellComponent,
  },
  // Остальной код компонента
};
</script>

<style scoped>
.container {
  background-color: #fffefb;
}

.profile {
  padding: 20px;
}

.avatar {
  width: 100px; /* Изменяем размер аватара для мобильного интерфейса */
}

.username {
  font-size: 1.5em; /* Увеличиваем размер имени пользователя для мобильного интерфейса */
}

.user-details {
  display: flex;
  background-color: #d4eaf7;
  height: 80px;
  width: 100%;
  border-radius: 15px;
  justify-content: space-between;
}

.bio {
  margin-top: 15px;
}

.user-image-full-name {
  display: flex;
  align-items: center;
  justify-content: center;
  padding-bottom: 20px;
}

.avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  margin-right: 10px;
}

.bell {
  position: absolute; /* Устанавливаем позиционирование absolute для .news-bell */
  right: 10px; /* Выравниваем правый край .news-bell по правому краю .user-image-full-name */
}

.numberSheetsPrinted,
.amountMoneySpent {
  flex: 1;
  text-align: center; /* Для выравнивания текста по центру, если необходимо */
  margin-top: 5px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.user-details-span {
  margin: 2px;
}

.user-details-span-detail {
  font-size: 16px;
}
</style>
