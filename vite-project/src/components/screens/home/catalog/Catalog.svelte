<script lang="ts">
	import CatalogItem from './CatalogItem.svelte'
	import { currentFilter, searchTerm } from '../../../../store.ts'

	import type { IRestaurant } from './restaurant.interface.ts'

	const restaurants: IRestaurant[] = [
		{
			img: 'https://www.hotelmousai.com/blog/wp-content/uploads/2021/12/Top-10-Traditional-Foods-in-Italy.jpg',
			destination: 1,
			slug: 'the-james-soho',
			name: 'The James SoHo',
			kitchens: ['Italian', 'Japanese'],
			priceRating: '$$$',
			rating: 4.7,
			type: 'Cafe'
		},
		{
			img: 'https://www.foodandwine.com/thmb/aTAmotbtG72fdSN7Lw077Jv5Flg=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/lobster-thermidor-FT-RECIPE0621-74e5a3b2e07d488bb03b5868b389877f.jpg',
			destination: 2,
			slug: 'la-petite-maison',
			name: 'La Petite Maison',
			kitchens: ['French', 'Mediterranean'],
			priceRating: '$$$$',
			rating: 4.8,
			type: 'Cinema'
		},
		{
			img: 'https://www.tastingtable.com/img/gallery/20-japanese-dishes-you-need-to-try-at-least-once/l-intro-1664219638.jpg',
			destination: 3,
			slug: 'sushi-nakazawa',
			name: 'Sushi Nakazawa',
			kitchens: ['Japanese', 'Sushi'],
			priceRating: '$$$$',
			rating: 4.9,
			type: 'Stand-up'
		},
		{
			img: 'https://media.cntraveler.com/photos/586eb8449d2b725a71af8123/master/pass/hot-dogs-gene-and-judes-photo-credit-Nick-Holmes.jpg',
			destination: 4,
			slug: 'blue-hill',
			name: 'Blue Hill',
			kitchens: ['American', 'Farm-to-Table'],
			priceRating: '$$$$',
			rating: 4.6,
			type: 'Ice cream'
		},
		{
			img: 'https://www.tastingtable.com/img/gallery/20-unique-california-foods-you-need-to-try/l-intro-1685033355.jpg',
			destination: 5,
			slug: 'chez-panisse',
			name: 'Chez Panisse',
			kitchens: ['Californian', 'Vegetarian'],
			priceRating: '$$$$',
			rating: 4.7,
			type: 'Cafe'
		}
	]

	let filterName = ''
	let filteredRestaurants = null
	currentFilter.subscribe(value => {
		filterName = value
		console.log('Текущий фильтр:', filterName)
		filteredRestaurants = restaurants.filter(
			restaurant => restaurant.type === filterName
		)
		if (value !== '') {
			searchTerm.set('') // Сбросить  serchterm
		}
	})

	searchTerm.subscribe(value => {
		const searchText = value.toLowerCase()
		filteredRestaurants = restaurants.filter(
			restaurant =>
				restaurant.name.toLowerCase().includes(searchText) ||
				restaurant.type.toLowerCase().includes(searchText) ||
				restaurant.kitchens.some(kitchen =>
					kitchen.toLowerCase().includes(searchText)
				)
		)
		if (value !== '') {
			currentFilter.set(null) // Сбросить выбранный фильтр
		}
	})
</script>

<div class="restaurants">
	{#each filteredRestaurants as restaurant (restaurant.name)}
		<CatalogItem {restaurant} />
	{/each}
</div>

<style lang="scss">
	.restaurants {
		@apply mt-8;
	}
</style>
