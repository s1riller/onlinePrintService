<script lang="ts">
	import FilterItem from './FilterItem.svelte'

	const filters = [
		{
			name: 'Cafe',
			icon: 'GiHamburger',
			color: '#FFB362',
			bgcolor: '#EAF2FF'
		},
		{
			name: 'Cinema',
			icon: 'GiPopcorn',
			color: '#E76B68',
			bgcolor: '#E4F6EA'
		},
		{
			name: 'Stand-up',
			icon: 'GiOldMicrophone',
			color: '#A8B0B9',
			bgcolor: '#FEEFEA'
		},
		{
			name: 'Ice cream',
			icon: 'GiIceCreamCone',
			color: '#D9BD83',
			bgcolor: '#FDF8E2'
		}
	]
</script>

<div class="filters">
	{#each filters as filter}
		<FilterItem {filter} />
	{/each}
</div>

<style lang="scss">
	.filters {
		@apply mt-6 flex items-center justify-between;
	}
</style>
