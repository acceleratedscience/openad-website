/**
 * Increase rotation speed as you scroll down
 */

// Detect scroll distance per step
let prevScroll = window.scrollY
let scroll = window.scrollY
let scrollDist = 0

// Molecule rotation speed
const autoRotMin = 0.05
const autoRotSensitivity = 50 // The distance you need to scroll to reach max rotation speed
const autoRotFactor = 2 // How much to speed up
let autoRotSpeed = autoRotMin
let autoRotTaperTmt = 0 // Timeout to taper of rotation speed

// Screens
const screens = Array.from(document.getElementsByClassName("screen"))
const screenMaxMarginTop = 20 // Expressed in vh! (viewport height)
const srceenMaxMarginSide = 20 // Expressed in vw! (viewport width)

// Background divs
const bgFeatures = document.getElementById("bg-features")
const bgEnterprise = document.getElementById("bg-enterprise")
const bgStudents = document.getElementById("bg-students")

// Scroll handler
let onScrollDebounced = _.throttle(onScroll, 100)
window.addEventListener("scroll", onScrollDebounced)
onScrollDebounced() // Trigger scroll on page load

function onScroll() {
	// Detect scroll distance
	prevScroll = scroll
	scroll = window.scrollY
	scrollDist = scroll - prevScroll

	/**
	 * Control molecule rotation speed
	 */

	// Inscrease rotation based on your scroll speed, then taper off
	setRotSpeed()

	/**
	 * Control UI screens
	 */

	// const pct2 = (scroll - window.innerHeight) / window.innerHeight
	const pct2 = scroll / window.innerHeight
	const marginSide = Math.max(srceenMaxMarginSide * (1 - pct2), 0)
	screens.forEach((screen, i) => {
		const marginTop = screenMaxMarginTop * (1 - pct2) * i
		screen.style.marginTop = `${marginTop}vh`
	})
	screens[0].style.marginRight = `-${marginSide}vw`
	screens[1].style.marginLeft = `-${marginSide}vw`

	/**
	 * Control backgrounds opacity
	 */

	// Positions
	const wHeight = window.innerHeight
	const posFeatures = document.getElementById("block-features").offsetTop
	const posEnterprise = document.getElementById("block-enterprise").offsetTop
	const posStudents = document.getElementById("block-students").offsetTop

	// Percentages
	const pctFeatures = (scroll + wHeight - posFeatures) / wHeight
	const pctEnterprise = (scroll + wHeight - posEnterprise) / wHeight
	const pctStudents = (scroll + wHeight - posStudents) / wHeight

	// Backgrounds
	if (pctFeatures > 0 && pctFeatures < 1) {
		bgFeatures.style.opacity = pctFeatures
	} else if (pctFeatures < 0) {
		bgFeatures.style.opacity = 0
	} else if (pctFeatures > 1) {
		bgFeatures.style.opacity = 1
	}
	if (pctEnterprise > 0 && pctEnterprise < 1) {
		bgEnterprise.style.opacity = pctEnterprise
	} else if (pctEnterprise < 0) {
		bgEnterprise.style.opacity = 0
	} else if (pctEnterprise > 1) {
		bgEnterprise.style.opacity = 1
	}
	if (pctStudents > 0 && pctStudents < 1) {
		bgStudents.style.opacity = pctStudents
	} else if (pctStudents < 0) {
		bgStudents.style.opacity = 0
	} else if (pctStudents > 1) {
		bgStudents.style.opacity = 1
	}
}

// Slow down rotation back to normal if no scrolliong detected
function setRotSpeed() {
	const prevAutoRotSpeed = autoRotSpeed

	// Calculate proposed rotation speed based on scroll distance
	const proposedAutoRotSpeed =
		autoRotMin +
		(Math.min(Math.abs(scrollDist), autoRotSensitivity) /
			autoRotSensitivity) * // Normalize to 0-1
			autoRotFactor // Multiply by factor

	// Only apply the new speed if it's greated than the previous one.
	// This is to avoid  that scrolling slowly would slow down the rotation.
	if (proposedAutoRotSpeed > prevAutoRotSpeed) {
		autoRotSpeed = proposedAutoRotSpeed
		viewer.settings.set("autoRotation", autoRotSpeed)
		_taper()
	}

	// Taper off rotation speed
	function _taper() {
		clearTimeout(autoRotTaperTmt)
		autoRotTaperTmt = setTimeout(() => {
			autoRotSpeed = Math.max(autoRotSpeed * 0.93, autoRotMin)
			viewer.settings.set("autoRotation", autoRotSpeed)
			// console.log(autoRotSpeed)
			if (autoRotSpeed > autoRotMin) _taper()
		}, 100)
	}
}
