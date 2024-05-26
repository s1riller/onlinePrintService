<script>
	import { push } from 'svelte-spa-router'
	export let title = 'Здесб должно быть название окна'
	export let pathBack = ''
	let isMenuOpen = false
</script>

<nav
	class="fixed top-0 left-0 right-0 border-gray-200 bg-gray-50 dark:bg-gray-800 dark:border-gray-700 z-50"
>
	<div
		class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4"
	>
		{#if pathBack}
			<button
				class="flex items-center justify-center"
				on:click={() => push(pathBack)}
			>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					viewBox="0 0 512 512"
					class="fill-white w-8 h-8"
					><path
						d="M217.9 256L345 129c9.4-9.4 9.4-24.6 0-33.9-9.4-9.4-24.6-9.3-34 0L167 239c-9.1 9.1-9.3 23.7-.7 33.1L310.9 417c4.7 4.7 10.9 7 17 7s12.3-2.3 17-7c9.4-9.4 9.4-24.6 0-33.9L217.9 256z"
					></path></svg
				>
			</button>
		{/if}

		<span
			class="self-center text-2xl font-semibold ml-10 whitespace-nowrap dark:text-white font-sans font-light"
		>
			{title}
		</span>

		<button
			type="button"
			class="inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
			aria-controls="navbar-solid-bg"
			aria-expanded={isMenuOpen}
			on:click={() => (isMenuOpen = !isMenuOpen)}
		>
			<span class="sr-only">Open main menu</span>
			<svg
				class="w-5 h-5"
				aria-hidden="true"
				xmlns="http://www.w3.org/2000/svg"
				fill="none"
				viewBox="0 0 17 14"
			>
				<path
					stroke="currentColor"
					stroke-linecap="round"
					stroke-linejoin="round"
					stroke-width="2"
					d="M1 1h15M1 7h15M1 13h15"
				/>
			</svg>
		</button>
		<div
			class={`transition-height duration-300 ease-in-out overflow-hidden ${isMenuOpen ? 'max-h-screen' : 'max-h-0'} w-full md:max-h-none md:block md:w-auto`}
			id="navbar-solid-bg"
		>
			<ul
				class="flex flex-col font-medium mt-4 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-transparent dark:bg-gray-800 md:dark:bg-transparent dark:border-gray-700"
			>
				<li>
					<a
						href="#"
						class="block py-2 px-3 md:p-0 text-white bg-blue-700 rounded md:bg-transparent md:text-blue-700 md:dark:text-blue-500 dark:bg-blue-600 md:dark:bg-transparent"
						aria-current="page">Home</a
					>
				</li>
				<li>
					<a
						href="#"
						class="block py-2 px-3 md:p-0 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
						>Services</a
					>
				</li>
				<li>
					<a
						href="#"
						class="block py-2 px-3 md:p-0 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
						>Pricing</a
					>
				</li>
				<li>
					<a
						href="#"
						class="block py-2 px-3 md:p-0 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
						>Contact</a
					>
				</li>
				<li>
					<a
						href="#"
						class="block py-2 px-3 md:p-0 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
						>Profile</a
					>
				</li>
			</ul>
		</div>
	</div>
</nav>

<style>
	.block {
		display: block !important;
	}
	.hidden {
		display: none !important;
	}
	.transition-height {
		transition: max-height 0.3s ease-in-out;
	}
	.max-h-0 {
		max-height: 0;
	}
	.max-h-screen {
		max-height: 100vh;
	}
</style>
