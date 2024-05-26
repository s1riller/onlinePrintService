import { writable } from 'svelte/store'

function filterFunc() {
	const { subscribe, set, update } = writable<string | null>(null)

	return {
		subscribe,
		set: (value: string | null) => {
			set(null)
			setTimeout(() => {
				update(() => value)
			}, 1)
		},
		reset: () => set(null)
	}
}

export const currentFilter = filterFunc()

export const searchTerm = writable('')

export const selectionSectionBottomNavigation = writable()

export const personInfo = writable({
	name: 'Савелий',
	surname: 'Михеев',
	phoneNumber: '+79996442072',
	email: 'frobtobt@gmail.com',
	avatar:
		'https://sun9-34.userapi.com/impg/pkwo_EAZQYh50-ie85LMFTkCfdSvJrlX_6PCew/-UhVf7CiwB4.jpg?size=542x677&quality=95&sign=6f6d567efebfb380ee89aae28987862d&type=album'
})
