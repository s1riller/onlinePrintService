<template>
  <div :class="bellIconClass" tabindex="0">
    <svg
      version="1.1"
      xmlns="http://www.w3.org/2000/svg"
      xmlns:xlink="http://www.w3.org/1999/xlink"
      x="0px"
      y="0px"
      width="50px"
      height="30px"
      viewBox="0 0 50 30"
      enable-background="new 0 0 50 30"
      xml:space="preserve"
    >
      <g class="bell-icon__group">
        <path
          class="bell-icon__ball"
          id="ball"
          fill-rule="evenodd"
          stroke-width="1.5"
          clip-rule="evenodd"
          fill="none"
          stroke="#currentColor"
          stroke-miterlimit="10"
          d="M28.7,25 c0,1.9-1.7,3.5-3.7,3.5s-3.7-1.6-3.7-3.5s1.7-3.5,3.7-3.5S28.7,23,28.7,25z"
        />
        <path
          class="bell-icon__shell"
          id="shell"
          fill-rule="evenodd"
          clip-rule="evenodd"
          fill="#FFFFFF"
          stroke="#currentColor"
          stroke-width="2"
          stroke-miterlimit="10"
          d="M35.9,21.8c-1.2-0.7-4.1-3-3.4-8.7c0.1-1,0.1-2.1,0-3.1h0c-0.3-4.1-3.9-7.2-8.1-6.9c-3.7,0.3-6.6,3.2-6.9,6.9h0 c-0.1,1-0.1,2.1,0,3.1c0.6,5.7-2.2,8-3.4,8.7c-0.4,0.2-0.6,0.6-0.6,1v1.8c0,0.2,0.2,0.4,0.4,0.4h22.2c0.2,0,0.4-0.2,0.4-0.4v-1.8 C36.5,22.4,36.3,22,35.9,21.8L35.9,21.8z"
        />
      </g>
    </svg>
    <div v-if="amountNews > 0" class="notification-amount">
      <span>{{ amountNews }}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "NotificationBell",

  props: {
    amountNews: {
      type: Number, // Укажите тип данных, который вы ожидаете
    },
  },

  data() {
    return {
      bellIconClass: {
        "bell-icon": true,
        "animation-active": this.amountNews > -1,
      },
    };
  },
};
</script>

<style>
.bell-icon {
  position: relative;
  width: 60px;
  height: 60px;
  background: #fff;
  border-radius: 50%;
  display: flex;
}
.bell-icon svg {
  margin: auto;
  position: relative;
  right: 2%;
  width: 80%;
  height: 80%;
  stroke: rgba(0, 0, 0, 0.75);
}

.bell-icon .bell-icon__group {
  transform-origin: 50% 2px;
  transform: rotate(-8deg);
  animation-fill-mode: both;
  animation-iteration-count: 1;
  animation-timing-function: ease-in-out;
}
.bell-icon .bell-icon__ball {
  transform-origin: 50% 2px;
  transform: translateX(-6.5%);
  animation-fill-mode: both;
  animation-iteration-count: 1;
  animation-timing-function: ease-in-out;
}
.bell-icon,
.bell-icon {
  outline: none;
  box-shadow: 0 0 12px -8px rgba(0, 0, 0, 0.6);
}
.bell-icon .bell-icon__group,
.bell-icon .bell-icon__group {
  animation: animateGroup 2.3s infinite;
}
.bell-icon .bell-icon__ball,
.bell-icon .bell-icon__ball {
  animation: animateBall 2.3s infinite;
}
.bell-icon .notification-amount,
.bell-icon .notification-amount {
  opacity: 1;
  visibility: visible;
}
.bell-icon .notification-amount::before,
.bell-icon .notification-amount::before {
  animation-name: bounce;
  animation-delay: 450ms;
}
.notification-amount {
  opacity: 0;
  visibility: hidden;
  position: absolute;
  top: 5%;
  right: 10%;
  width: 25px;
  height: 25px;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: "Copse", serif;
  font-size: 14px;
}
.notification-amount span {
  position: relative;
}
.notification-amount::before {
  content: "";
  position: absolute;
  width: 100%;
  height: 100%;
  background-color: #f72918;
  border-radius: 50%;
  z-index: 0;
  transform: scale(0);
  animation-duration: 800ms;
  animation-fill-mode: both;
}
@keyframes animateGroup {
  0%,
  100% {
    transform: rotate(-8deg);
  }
  17.542% {
    transform: rotate(0deg);
  }
  35.084% {
    transform: rotate(-20deg);
  }
  48.2405% {
    transform: rotate(20deg);
  }
  57.0115% {
    transform: rotate(-20deg);
  }
  64.9054% {
    transform: rotate(8deg);
  }
  74.5535% {
    transform: rotate(-15deg);
  }
  78.939% {
    transform: rotate(-7deg);
  }
}
@keyframes animateBall {
  0%,
  100% {
    transform: translateX(-6.5%);
  }
  17.542% {
    transform: translateX(0%);
  }
  21.9275% {
    transform: translateX(-1%);
  }
  35.084% {
    transform: translateX(11%);
  }
  48.2405% {
    transform: translateX(-11%);
  }
  52.626% {
    transform: translateX(0%);
  }
  59.6428% {
    transform: translateX(10%);
  }
  68.4138% {
    transform: translateX(-11%);
  }
  78.939% {
    transform: translateX(11%);
  }
  85.9558% {
    transform: translateX(-11%);
  }
}
@keyframes bounce {
  0% {
    transform: scale(0);
  }
  14% {
    transform: scale(1.15);
  }
  28% {
    transform: scale(1);
  }
  42% {
    transform: scale(1.15);
  }
  70% {
    transform: scale(1);
  }
  100% {
    transform: scale(1);
  }
}
</style>
