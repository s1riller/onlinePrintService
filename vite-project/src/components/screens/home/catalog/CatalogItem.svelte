<script lang="ts">
	import { link } from 'svelte-spa-router'
	import type { IRestaurant } from './restaurant.interface.ts'
	import IoMdWallet from 'svelte-icons/io/IoMdWallet.svelte'
	import TiStarFullOutline from 'svelte-icons/ti/TiStarFullOutline.svelte'
	import GoPrimitiveDot from 'svelte-icons/go/GoPrimitiveDot.svelte'
	import { onMount } from 'svelte'
	export let restaurant: IRestaurant
	const {
		slug,
		rating,
		destination,
		img: src,
		kitchens,
		name,
		priceRating
	} = restaurant
</script>

<div class="restaurant">
	<a href use:link={`/restaurant/${slug}`}>
		<img {src} alt={name} />
		<div class="image-overlay"></div>
	</a>
	<div class="info">
		<div>
			<div class="heading">
				{name}
			</div>
			<div class="price">
				<div class="icon">
					<IoMdWallet />
				</div>
				<span>Average price {priceRating}</span>
			</div>
			<div class="kitchens">
				{#each kitchens as value, index}
					<div>
						{value}
					</div>
					{#if index !== kitchens.length - 1}
						<div style="width: 4px;">
							<GoPrimitiveDot />
						</div>
					{/if}
				{/each}
			</div>
		</div>
		<div>
			<div class="rating">
				<div class="star">
					<TiStarFullOutline />
				</div>
				<span>{rating}</span>
			</div>
			<div class="destination">
				{destination} km
			</div>
		</div>
	</div>
</div>

<style lang="scss">
	html,
	body {
		margin: 0;
		padding: 0;
		width: 100%;
		overflow-x: hidden; /* Скрыть горизонтальный скролл */
	}
	.restaurant {
		@apply mb-10 bg-white shadow-lg rounded-3xl relative;
		max-width: 100%; /* Гарантировать, что контейнер не выходит за пределы экрана */
		margin: 0 auto; /* Центрирование контейнера */
		overflow: hidden; /* Обрезать содержимое, выходящее за пределы контейнера */

		> a > img {
			@apply rounded-3xl w-full h-full;
		}
		.info {
			@apply flex justify-between text-[#111] p-3;

			display: flex;
			flex-wrap: wrap;
			overflow: hidden;
			box-sizing: border-box;

			.heading {
				@apply font-semibold text-2xl mb-2;
			}
			.price {
				@apply flex items-center;
				.icon {
					@apply w-5 mr-1.5;
				}
			}
		}

		.rating {
			@apply flex items-center;
			.star {
				@apply w-5 text-yellow-400;
			}
			> span {
				@apply inline-block ml-1 bg-slate-50 rounded-full py-1 px-2;
			}
		}

		.destination {
			@apply mt-3 bg-green-500 py-1 px-3 text-white text-sm rounded-lg;
		}
		.kitchens {
			@apply opacity-25 flex items-center mt-2 text-sm;
			> div {
				@apply mr-2;
			}
		}
		&::before,
		&::after {
			content: '';
			@apply h-full absolute rounded-3xl left-2;
			width: 100%;
			height: 94%;
			filter: blur(4px) opacity(0.8);

			> a > img {
				@apply rounded-3xl;
			}
		}
		&::before {
			@apply top-3;
			background-color: #c4ead8;
			transform: rotate(-10deg);
			z-index: -1;
		}
		&::after {
			@apply top-3;
			background-color: #dff2e8;
			transform: rotate(-13deg);
			z-index: -2;
		}
	}
	@media screen and (min-width: 500px) {
		.restaurant {
			max-width: 1500px; /* Пример ширины контейнера для больших экранов */
			margin: auto; /* Центрирование контейнера */
		}

		.restaurant > a > img {
			width: 100%; /* Ширина изображения занимает всю доступную ширину контейнера */
			height: auto; /* Высота изображения автоматически рассчитывается для поддержки соотношения сторон */
			transition: transform 0.3s ease; /* Анимация для изображения */
		}

		.restaurant:hover > a > img {
			transform: scale(1.05); /* Масштабирование изображения при наведении */
		}

		.info {
			padding: 20px; /* Увеличиваем внутренний отступ для информации о ресторане */
		}

		.info > div {
			height: 120%;
			width: 100%; /* Распределение информации о ресторане по ширине контейнера */
		}

		.kitchens {
			margin-top: 10px; /* Увеличиваем отступ между списком кухонь и остальной информацией */
		}

		.restaurant::before,
		.restaurant::after {
			width: 100%; /* Ширина тумана приспосабливается к размеру контейнера */
		}
	}
</style>
