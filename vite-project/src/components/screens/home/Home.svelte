<script lang="ts">
	import { link } from 'svelte-spa-router'
	import Search from './search/Search.svelte'
	import Filter from './filter/Filter.svelte'
	import Catalog from './catalog/Catalog.svelte'
</script>

<div>
	<Search />
	<Filter />
	<Catalog />
	<a href="/company/soho" use:link>Soho</a>
</div>
