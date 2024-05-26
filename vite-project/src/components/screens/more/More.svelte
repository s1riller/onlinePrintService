<script lang="ts">
	import Navbar from './components/Navbar.svelte'
	import Profilebar from './components/Profilebar.svelte'
	import InviteFriend from './components/InviteFriend.svelte'
</script>

<Navbar title="Меню приложения" />
<Profilebar />
<InviteFriend />
<div class="w-full mt-2 text-sm font-medium text-gray-900">
	<a
		href="#"
		class="block w-full px-4 py-2 border-b text-2xl font-normal border-gray-100 cursor-pointer hover:bg-gray-100 hover:text-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-500 dark:focus:text-white"
	>
		Избранные форматы
	</a>
	<a
		href="#"
		class="block w-full px-4 py-2 border-b text-2xl font-normal border-gray-100cursor-pointer hover:bg-gray-100 hover:text-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-500 dark:focus:text-white"
	>
		Мои заказы
	</a>
	<a
		href="#"
		class="block w-full px-4 py-2 border-b text-2xl font-normal border-gray-100cursor-pointer hover:bg-gray-100 hover:text-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-500 dark:focus:text-white"
	>
		Служба поддержки
	</a>
	<a
		href="#"
		class="block w-full px-4 py-2 border-b text-2xl font-normal border-gray-100cursor-pointer hover:bg-gray-100 hover:text-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-500 dark:focus:text-white"
	>
		Подробности о сайте
	</a>
	<a
		href="#"
		class="block w-full px-4 py-2 rounded-b-lg text-2xl font-normal cursor-pointer hover:bg-gray-100 hover:text-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-500 dark:focus:text-white text-red-600"
	>
		Выйти из профиля
	</a>
</div>
