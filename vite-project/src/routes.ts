/* This TypeScript code snippet is importing two components, `Home` and `Restautant`, from their
respective Svelte files located in the `components/screens/home` and `components/screens/restautant`
directories. These components are then assigned to specific routes in the `routes` object. */
import Home from './components/screens/home/Home.svelte'
import Restaurant from './components/screens/restautant/Restautant.svelte'
import NotFound from './components/screens/NotFound.svelte'
import Main from './components/screens/main/Main.svelte'
import More from './components/screens/more/More.svelte'
import Profile from './components/screens/more/Profile.svelte'
import Print from './components/screens/print/Print.svelte'
export const routes = {
	'/': Home,
	'/restaurant/:name': Restaurant,
	'/print': Print,
	'/main': Main,
	'/more': More,
	'/more/me': Profile,
	'*': NotFound
}
