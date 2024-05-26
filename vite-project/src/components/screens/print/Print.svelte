<script lang="ts">
	import Navbar from '../more/components/Navbar.svelte'
	import FileInput from './components/FileInput.svelte'
	import { Modal } from 'flowbite'
	import type { ModalOptions, ModalInterface } from 'flowbite'
	import GetUserMedia from './components/GetUserMedia.svelte'
</script>

<Navbar title="Печать документа" />

<div class="sm:hidden pt-20">
	<label for="tabs" class="sr-only">Select your country</label>
	<select
		id="tabs"
		class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
	>
		<option>Profile</option>
		<option>Dashboard</option>
	</select>
</div>
<ul
	class=" text-sm font-medium text-center text-gray-500 rounded-lg shadow sm:flex dark:divide-gray-700 dark:text-gray-400"
>
	<li class="w-full focus-within:z-10">
		<FileInput />
	</li>
	<li class="w-full focus-within:z-10">
		<GetUserMedia />
	</li>
</ul>
