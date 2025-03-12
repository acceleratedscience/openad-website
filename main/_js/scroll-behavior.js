/**
 * Increase rotation speed as you scroll down
 */

// Molecule rotation speed
const autoRotMin = 0.05
const autoRotMax = 0.5
const autoRotRange = autoRotMax - autoRotMin
const scrollRange = 1000 // The distance over which the rotation speed increases

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

function onScroll() {
	const scroll = window.scrollY

	/**
	 * Control molecule rotation speed
	 */

	const pct1 = scroll / scrollRange
	if (scroll < scrollRange) {
		viewer.settings.set("autoRotation", autoRotMin + autoRotRange * pct1)
	} else {
		viewer.settings.set("autoRotation", 1)
	}

	/**
	 * Control screens
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
