<script lang="ts">
	import {
		GiHamburger,
		GiPopcorn,
		GiOldMicrophone,
		GiIceCreamCone
	} from 'svelte-icons/gi'

	import type { IFilter } from './filter.Interface.ts'

	import { currentFilter } from '../../../../store.ts'

	export let filter: IFilter

	const iconMap = {
		GiHamburger,
		GiPopcorn,
		GiOldMicrophone,
		GiIceCreamCone
	}

	let Icon = iconMap[filter.icon] || GiHamburger
	let cu
	let isActive = false

	currentFilter.subscribe(value => {
		isActive = value === filter.name
		cu = value
	})

	function toggleFilter() {
		if (cu === filter.name) {
			currentFilter.reset()
		} else {
			currentFilter.set(filter.name)
		}
	}
</script>

<button class:active={isActive} class="filter" on:click={toggleFilter}>
	<span
		class="icon"
		style="color: {filter.color}; background-color:{filter.bgcolor}"
	>
		<Icon />
	</span>

	<span class="name" class:activeText={isActive}>
		{filter.name}
	</span>
</button>

<style lang="scss">
	.filter {
		@apply text-center bg-white rounded-3xl p-2;
		box-shadow: 0 3px 6px rgba(0, 0, 0, 0.05);
		width: 4.5rem;

		&.active {
			@apply bg-slate-900;
		}

		.icon {
			@apply rounded-3xl flex items-center justify-center p-3.5;
		}

		.name {
			@apply mt-1 block;
			font-size: 12px;

			&.activeText {
				@apply text-indigo-50;
			}
		}
	}
</style>
