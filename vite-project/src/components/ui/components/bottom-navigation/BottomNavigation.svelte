<script lang="ts">
	import { push } from 'svelte-spa-router'
	import IoIosPrint from 'svelte-icons/io/IoIosPrint.svelte'
	import { onMount } from 'svelte'
	import { fade, fly } from 'svelte/transition'
	import { writable } from 'svelte/store'

	let visible = null

	import { selectionSectionBottomNavigation } from '../../../../store.ts'
</script>

<div
	class="fixed bottom-0 left-0 z-50 w-full h-16 bg-white border-t dark:border-white shadow"
>
	<div class="grid h-full max-w-lg grid-cols-4 mx-auto font-medium">
		<button
			type="button"
			class="inline-flex items-center justify-between px-5 hover:bg-gray-50 dark:hover:bg-blue-100 rounded-full group"
			class:active={$selectionSectionBottomNavigation === 0}
			on:click={() => {
				selectionSectionBottomNavigation.set(0)
				push('/main')
			}}
		>
			<svg
				xmlns="http://www.w3.org/2000/svg"
				viewBox="0 0 512 512"
				class="svelte-c8tyih w-8 svg-icon-blue mr-2"
				><path
					d="M128 248v200c0 8.8 7.2 16 16 16h224c8.8 0 16-7.2 16-16V248c0-8.8-7.2-16-16-16H144c-8.8 0-16 7.2-16 16zM384 48H128c-8.8 0-16 7.2-16 16v20c0 2.2 1.8 4 4 4h280c2.2 0 4-1.8 4-4V64c0-8.8-7.2-16-16-16z"
				></path>
				<path
					d="M432.5 112h-352C62.9 112 48 125.8 48 143.3v174.4c0 17.5 14.9 32.3 32.5 32.3H96c4.4 0 8-3.6 8-8V236c0-15.5 12.5-28 28-28h248c15.5 0 28 12.5 28 28v106c0 4.4 3.6 8 8 8h16.5c17.6 0 31.5-14.8 31.5-32.3V143.3c0-17.5-13.9-31.3-31.5-31.3z"
				></path>
			</svg>
			{#if $selectionSectionBottomNavigation === 0}
				<span
					in:fly={{ y: 200, duration: 2000 }}
					out:fade
					class=" text-sm text-gray-500 dark:text-gray-400 group-hover:text-blue-100 dark:group-hover:text-blue-500"
				>
					Принтеры
				</span>
			{/if}
		</button>

		<button
			type="button"
			class="inline-flex items-center justify-between px-5 hover:bg-gray-50 dark:hover:bg-blue-100 rounded-full group"
			class:active={$selectionSectionBottomNavigation === 1}
			on:click={() => {
				selectionSectionBottomNavigation.set(1)
				push('/print')
			}}
		>
			<svg
				xmlns="http://www.w3.org/2000/svg"
				viewBox="0 0 512 512"
				class="svelte-c8tyih w-8 svg-icon-blue mr-2"
				><path
					d="M352 115h90c3.3 0 6-2.7 6-6 0-8.2-3.7-16-10-21.3l-77.1-64.2c-4.9-4.1-14.2-7.4-20.6-7.4-4.1 0-7.4 3.3-7.4 7.4V96c.1 10.5 8.6 19 19.1 19z"
				></path>
				<path
					d="M307 96V16H176c-17.6 0-32 14.4-32 32v336c0 17.6 14.4 32 32 32h240c17.6 0 32-14.4 32-32V141h-96c-24.8 0-45-20.2-45-45z"
				></path>
				<path
					d="M116 412V80H96c-17.6 0-32 14.4-32 32v352c0 17.6 14.4 32 32 32h256c17.6 0 32-14.4 32-32v-20H148c-17.6 0-32-14.4-32-32z"
				></path></svg
			>
			{#if $selectionSectionBottomNavigation === 1}
				<span
					in:fly={{ y: 200, duration: 2000 }}
					out:fade
					class=" text-sm text-gray-500 dark:text-gray-400 group-hover:text-blue-100 dark:group-hover:text-blue-500"
				>
					Печать
				</span>
			{/if}
		</button>
		<button
			type="button"
			class="inline-flex items-center justify-between px-5 hover:bg-gray-50 dark:hover:bg-blue-100 rounded-full group"
			on:click={() => {
				selectionSectionBottomNavigation.set(2)
			}}
		>
			<svg
				xmlns="http://www.w3.org/2000/svg"
				viewBox="0 0 512 512"
				class="svelte-c8tyih w-8 svg-icon-blue mr-2"
				class:active={$selectionSectionBottomNavigation === 2}
				><path
					d="M359.1 231.9h-.1c-.1-.1-.3-.4-.4-.6l-78.9-79.6c-5.8-6-14.2-10.2-23.6-10.2-11.8 0-22.2 6.2-27.7 16.3 0 0-3.4 5.1-12.6 19.8-1.6 2.6-1.6 6 .1 8.6l26.8 41.2c2.9 3.8 3.3 8 1.4 9.9l-.1.1c-2.3 2.3-5.9 1.5-9.8-1.4l-32.3-20.5c-3.8-2.4-8.7-1.2-11.1 2.5-21.9 35.1-46.8 74.7-71.2 114-1.6 2.5-1.6 5.7-.1 8.3l14.1 24.1c2.9 3.8 3.3 8 1.4 9.9l-.1.1c-2.3 2.3-5.9 1.5-9.8-1.4l-16.6-8.4c-3.7-1.9-8.2-.6-10.4 2.9-17.7 28.3-28 44.7-29.1 46.5-3 5.1-5 11.2-5 17.8 0 17.8 14.2 32.2 31.9 32.2 7.8 0 14.4-3.4 20.6-7.6L221 378.8c3.4-2.5 4.2-7.2 2-10.7L202.5 336c-2.9-3.8-3.3-8-1.4-9.9l.1-.1c2.3-2.3 5.9-1.5 9.8 1.4l37.4 25.6c2.8 1.9 6.5 1.9 9.3-.2 53-39.1 97.5-72.2 97.5-72.2 7.9-6 13-15.4 13-26 0-8.7-3.1-16.8-9.1-22.7zM446.9 131.2l-11.2-17.9c-2.2-3.8-7.1-5.1-10.9-2.9L365.4 147l47.3-78.9c2.2-3.8.9-8.8-2.9-11l-17.7-8c-3.9-2.3-8.8-.9-11 3l-57.6 108.3 28.6 28.8 91.8-46.8c3.9-2.2 5.3-7.2 3-11.2z"
				></path></svg
			>
			{#if $selectionSectionBottomNavigation === 2}
				<span
					in:fly={{ y: 200, duration: 2000 }}
					out:fade
					class=" text-sm text-gray-500 dark:text-gray-400 group-hover:text-blue-100 dark:group-hover:text-blue-500"
				>
					Магазин
				</span>
			{/if}
		</button>
		<button
			type="button"
			class="inline-flex items-center justify-between px-5 hover:bg-gray-50 dark:hover:bg-blue-100 rounded-full group"
			class:active={$selectionSectionBottomNavigation === 3}
			on:click={() => {
				selectionSectionBottomNavigation.set(3)
				push('/more')
			}}
		>
			<svg
				xmlns="http://www.w3.org/2000/svg"
				viewBox="0 0 512 512"
				class="svelte-c8tyih w-8 svg-icon-blue mr-3"
				><path
					d="M255.8 218c-21 0-38 17-38 38s17 38 38 38 38-17 38-38-17-38-38-38zM102 218c-21 0-38 17-38 38s17 38 38 38 38-17 38-38-17-38-38-38zM410 218c-21 0-38 17-38 38s17 38 38 38 38-17 38-38-17-38-38-38z"
				></path></svg
			>
			{#if $selectionSectionBottomNavigation === 3}
				<span
					in:fly={{ y: 200, duration: 2000 }}
					out:fade
					class=" text-sm text-gray-500 dark:text-gray-400 group-hover:text-blue-100 dark:group-hover:text-blue-500"
				>
					Еще
				</span>
			{/if}
		</button>
	</div>
</div>

<style lang="scss">
	.svg-icon-blue {
		fill: #63b4ff;
	}

	.active {
		@apply bg-blue-100;
	}
</style>
