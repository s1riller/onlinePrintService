<script lang="ts">
	import Router from 'svelte-spa-router'
	import { routes } from './routes.ts'
	import BottomNavigation from './components/ui/components/bottom-navigation/BottomNavigation.svelte'
</script>

<main>
	<Router {routes} useHash={false} />
	<BottomNavigation />
</main>
