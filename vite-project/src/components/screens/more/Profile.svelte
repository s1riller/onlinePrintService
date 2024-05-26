<script lang="ts">
	import { personInfo } from '../../../store.ts'
	import { onMount } from 'svelte'
	import Navbar from './components/Navbar.svelte'
	import InputPhoneNumber from './components/InputPhoneNumber.svelte'
	// Создаем локальные переменные для информации о человеке
	let name = ''
	let surname = ''
	let phoneNumber = ''
	let email = ''
	let avatar = ''

	// Подписываемся на изменения в хранилище с информацией о человеке
	personInfo.subscribe(value => {
		// Обновляем локальные переменные с информацией о человеке
		name = value.name
		surname = value.surname
		phoneNumber = value.phoneNumber
		email = value.email
		avatar = value.avatar
	})

	let editing = false

	function toggleEdit() {
		editing = !editing
	}

	// Функция для сохранения изменений
	function saveChanges() {
		const updatedInfo = {
			name,
			surname,
			phoneNumber,
			email,
			avatar
		}
		// Отправить обновленную информацию в хранилище
		personInfo.set(updatedInfo)
		toggleEdit() // Закрыть режим редактирования
	}
</script>

<Navbar pathBack="/more" title="Профиль" />

<div class="container mx-auto p-5 mt-20">
	<div class="grid grid-cols-1 md:grid-cols-2 gap-5">
		<div>
			<img
				src={avatar}
				alt="Аватар"
				class="rounded-full w-24 h-24 mx-auto overflow-hidden"
			/>

			{#if editing}
				<div class="mt-4">
					<label for="name" class="block text-gray-700">Имя:</label>
					<input
						type="text"
						id="name"
						bind:value={name}
						class="mt-1 p-2 border rounded-lg w-full"
					/>
				</div>

				<div class="mt-4">
					<label for="surname" class="block text-gray-700">Фамилия:</label>
					<input
						type="text"
						id="surname"
						bind:value={surname}
						class="mt-1 p-2 border rounded-lg w-full"
					/>
				</div>

				<div class="mt-4">
					<label for="phoneNumber" class="block text-gray-700"
						>Номер телефона:</label
					>
					<InputPhoneNumber />
				</div>

				<div class="mt-4">
					<label for="email" class="block text-gray-700">Email:</label>
					<input
						type="email"
						id="email"
						bind:value={email}
						class="mt-1 p-2 border rounded-lg w-full"
					/>
				</div>

				<div class="mt-4 flex justify-center">
					<button
						type="button"
						class="bg-blue-500 text-white px-4 py-2 rounded-lg mr-2"
						on:click={saveChanges}>Сохранить</button
					>
					<button
						type="button"
						class="bg-gray-500 text-white px-4 py-2 rounded-lg"
						on:click={toggleEdit}>Отмена</button
					>
				</div>
			{:else}
				<h2 class="text-3xl font-bold text-center mt-4">{name} {surname}</h2>
				<p class="text-lg text-center mt-2">{phoneNumber}</p>
				<p class="text-lg text-center mt-2">{email}</p>
				<div class="mt-4 flex justify-center">
					<button
						type="button"
						class="text-white bg-blue-700 hover:bg-blue-800
            focus:ring-4 focus:outline-none focus:ring-blue-300
             font-medium rounded-full text-sm p-2.5 text-center
             flex justify-start items-start me-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
						on:click={toggleEdit}
					>
						<span>Изменить</span></button
					>
				</div>
			{/if}
		</div>
	</div>
</div>

<ul class="w-full text-sm font-medium text-gray-900 shadow">
	<li
		class="w-full px-4 py-4 border-gray-200 rounded-t-lg dark:border-gray-600 flex justify-between"
	>
		<span>Я хочу получать информационную рассылку</span>
		<label class="inline-flex items-center mb-5 cursor-pointer">
			<input type="checkbox" value="" class="sr-only peer" />
			<div
				class="relative w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 dark:peer-focus:ring-blue-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:w-5 after:h-5 after:transition-all dark:border-gray-600 peer-checked:bg-blue-600"
			></div>
		</label>
	</li>

	<li
		class="w-full px-4 py-4 border-gray-200 dark:border-gray-600 flex justify-between"
	>
		<span>Я хочу получать уведомления</span>
		<label class="inline-flex items-center mb-5 cursor-pointer pl-5">
			<input type="checkbox" value="" class="sr-only peer" />
			<div
				class="relative w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 dark:peer-focus:ring-blue-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:w-5 after:h-5 after:transition-all dark:border-gray-600 peer-checked:bg-blue-600"
			></div>
		</label>
	</li>
	<li
		class="w-full px-4 py-4 border-gray-200 dark:border-gray-600 flex justify-between"
	>
		<span>Я хочу получать CMC</span>
		<label class="inline-flex items-center mb-5 cursor-pointer pl-5">
			<input type="checkbox" value="" class="sr-only peer" />
			<div
				class="relative w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 dark:peer-focus:ring-blue-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:w-5 after:h-5 after:transition-all dark:border-gray-600 peer-checked:bg-blue-600"
			></div>
		</label>
	</li>
</ul>

<div class="flex justify-center items-center">
	<button
		type="button"
		class=" text-white bg-gradient-to-r from-red-400 via-red-500 to-red-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-red-300 dark:focus:ring-red-800 shadow-lg shadow-red-500/50 dark:shadow-lg dark:shadow-red-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2 mt-8 flex justify-between items-center"
	>
		<svg
			xmlns="http://www.w3.org/2000/svg"
			viewBox="0 0 512 512"
			class="svelte-c8tyih w-8 h-8 fill-white"
		>
			<path
				d="M133.1 128l23.6 290.7c0 16.2 13.1 29.3 29.3 29.3h141c16.2 0 29.3-13.1 29.3-29.3L379.6 128H133.1zm61.6 265L188 160h18.5l6.9 233h-18.7zm70.3 0h-18V160h18v233zm52.3 0h-18.6l6.8-233H324l-6.7 233zM364 92h-36l-26.3-23c-3.7-3.2-8.4-5-13.2-5h-64.8c-4.9 0-9.7 1.8-13.4 5L184 92h-36c-17.6 0-30 8.4-30 26h276c0-17.6-12.4-26-30-26z"
			></path>
		</svg>
		<span>Удалить аккаунт</span>
	</button>
</div>
