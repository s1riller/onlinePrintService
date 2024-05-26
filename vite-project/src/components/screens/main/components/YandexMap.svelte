<script lang="ts">
	import { onMount } from 'svelte'

	export const LOCATION = {
		center: [55.75254, 37.623082], // starting position [lat, lng]
		zoom: 9 // starting zoom
	}

	// Array containing data for markers
	export const markerProps = [
		{
			coordinates: [55.752, 37.623],
			iconSrc:
				'https://sun9-58.userapi.com/impg/kmPIZR0DpxmjNXj5cbiGudfXL1DE8wq6ngEomw/Vo1F3Di8CSo.jpg?size=542x677&quality=95&sign=0141db49bb1aa3b2e8ce2ee3001d2b92&type=album',
			message: "I'm yellow capybara!",
			htmlContent:
				"<div class='icon-marker' style='padding: 20px;'>This is the yellow capybara!</div>"
		},
		{
			coordinates: [55.622, 38.125],
			iconSrc:
				'https://sun9-58.userapi.com/impg/kmPIZR0DpxmjNXj5cbiGudfXL1DE8wq6ngEomw/Vo1F3Di8CSo.jpg?size=542x677&quality=95&sign=0141db49bb1aa3b2e8ce2ee3001d2b92&type=album',
			message: "I'm purple capybara!",
			htmlContent:
				"<div class='icon-marker' style='padding: 20px;'>This is the purple capybara!</div>"
		},
		{
			coordinates: [55.415, 37.295],
			iconSrc:
				'https://sun9-58.userapi.com/impg/kmPIZR0DpxmjNXj5cbiGudfXL1DE8wq6ngEomw/Vo1F3Di8CSo.jpg?size=542x677&quality=95&sign=0141db49bb1aa3b2e8ce2ee3001d2b92&type=album',
			message: "I'm green capybara!",
			htmlContent:
				"<div class='icon-marker' style='padding: 20px;'>This is the green capybara!</div>"
		}
	]

	let map = null
	let Loaded = false
	let activeHtmlContent = ''
	let activeAddress = ''

	onMount(() => {
		const script = document.createElement('script')
		script.src =
			'https://api-maps.yandex.ru/2.1/?lang=ru_RU&apikey=0e7cb141-1ff6-44db-b891-1b8c0b7dd740'
		script.type = 'text/javascript'
		script.onload = () => {
			ymaps.ready(initMap)
		}
		document.head.appendChild(script)
	})

	function initMap() {
		map = new ymaps.Map('map', {
			center: LOCATION.center,
			zoom: LOCATION.zoom
		})

		// Adding markers from markerProps with custom icons
		markerProps.forEach(markerProp => {
			const placemark = new ymaps.Placemark(
				markerProp.coordinates,
				{
					balloonContent: markerProp.message
				},
				{
					iconLayout: 'default#image',
					iconImageHref: markerProp.iconSrc,
					iconImageSize: [30, 42],
					iconImageOffset: [-15, -42]
				}
			)
			placemark.events.add('click', () => {
				activeHtmlContent = markerProp.htmlContent
				getAddress(markerProp.coordinates)
			})
			map.geoObjects.add(placemark)
		})

		Loaded = true
	}

	function getAddress(coordinates) {
		ymaps.geocode(coordinates).then(result => {
			const firstGeoObject = result.geoObjects.get(0)
			activeAddress = firstGeoObject.getAddressLine()
			document.getElementById('bottom-panel').style.display = 'block'
		})
	}

	function closePanel() {
		activeHtmlContent = ''
		activeAddress = ''
		document.getElementById('bottom-panel').style.display = 'none'
	}
</script>

<div class="container">
	{#if !Loaded}
		<h1>Loading...</h1>
	{/if}
	<div id="map"></div>
	<div id="bottom-panel">
		<button id="close-button" on:click={closePanel}>Close</button>
		<div>{activeAddress}</div>
		<!-- {@html activeHtmlContent} -->
	</div>
</div>

<style lang="scss">
	.container {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		width: 100%;
		height: 100%; /* Make the container take full height */
	}

	#map {
		width: 100%;
		height: 70vh; /* Make map take 70% of the viewport height */
	}

	#bottom-panel {
		display: none; /* Initially hidden */
		position: fixed;
		bottom: 70px;
		width: 100%;
		background-color: white;
		box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
		z-index: 1000;
		padding: 10px;
	}

	#close-button {
		position: absolute;
		top: 10px;
		right: 10px;
		padding: 5px 10px;
		background-color: red;
		color: white;
		border: none;
		border-radius: 5px;
		cursor: pointer;
	}

	html,
	body {
		width: 100%;
		height: 100%;
		margin: 0;
		padding: 0;
		font-family: Arial, Helvetica, sans-serif;
		overflow: hidden; /* Prevent scrolling */
	}

	.icon-marker {
		cursor: pointer;
		width: 75px;
		height: 75px;
		border-radius: 50%;
		position: relative;
		transform: translate(-50%, -50%);
	}
</style>
