<script lang="ts">
	import { onMount } from 'svelte'

	let videoElement: HTMLVideoElement
	let canvasElement: HTMLCanvasElement
	let videoStream: MediaStream

	onMount(() => {
		startCamera()
	})

	async function startCamera() {
		try {
			videoStream = await navigator.mediaDevices.getUserMedia({
				video: { facingMode: 'environment' }
			})
			videoElement.srcObject = videoStream
			await videoElement.play()
		} catch (err) {
			console.error('Error accessing camera: ', err)
		}
	}

	function captureImage() {
		const context = canvasElement.getContext('2d')
		canvasElement.width = videoElement.videoWidth
		canvasElement.height = videoElement.videoHeight
		context.drawImage(
			videoElement,
			0,
			0,
			canvasElement.width,
			canvasElement.height
		)
		const imageData = canvasElement.toDataURL('image/png')
		console.log('Captured Image Data URL:', imageData)

		// Optionally, stop the camera after capturing the image
		stopCamera()
	}

	function stopCamera() {
		videoStream.getTracks().forEach(track => track.stop())
	}
</script>

<div id="camera-container">
	<video bind:this={videoElement} autoplay></video>
	<button on:click={captureImage}>Capture Image</button>
	<canvas bind:this={canvasElement}></canvas>
</div>

<style>
	#camera-container {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		width: 100%;
		height: 100%;
	}

	video {
		width: 100%;
		max-width: 600px;
		height: auto;
		border: 1px solid #ccc;
		margin-bottom: 10px;
	}

	canvas {
		display: none;
	}
</style>
