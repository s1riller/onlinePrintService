<script lang="ts">
	import { push } from 'svelte-spa-router'
</script>

<div class="flex items-center gap-4 mt-16 bg-black p-2">
	<img
		class="w-8 h-8 rounded-full"
		src="https://sun9-34.userapi.com/impg/pkwo_EAZQYh50-ie85LMFTkCfdSvJrlX_6PCew/-UhVf7CiwB4.jpg?size=542x677&quality=95&sign=6f6d567efebfb380ee89aae28987862d&type=album"
		alt=""
	/>
	<div class="font-medium text-white">
		<div>Jese Leos</div>
		<div class="text-sm text-gray-500 dark:text-gray-400">
			Присоединился в Августе 2014
		</div>
	</div>
	<div class="ml-auto">
		<button
			class="flex items-center justify-center"
			on:click={() => push('/more/me')}
		>
			<svg
				xmlns="http://www.w3.org/2000/svg"
				viewBox="0 0 512 512"
				class="fill-white w-8 h-8"
			>
				<path
					d="M294.1 256L167 129c-9.4-9.4-9.4-24.6 0-33.9s24.6-9.3 34 0L345 239c9.1 9.1 9.3 23.7.7 33.1L201.1 417c-4.7 4.7-10.9 7-17 7s-12.3-2.3-17-7c-9.4-9.4-9.4-24.6 0-33.9l127-127.1z"
				></path>
			</svg>
		</button>
	</div>
</div>
