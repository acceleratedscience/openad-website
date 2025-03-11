window.addEventListener("scroll", onScroll)

const bgFeatures = document.getElementById("bg-features")
const bgEnterprise = document.getElementById("bg-enterprise")
const bgStudents = document.getElementById("bg-students")

function onScroll() {
	// Positions
	const scroll = window.scrollY
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
