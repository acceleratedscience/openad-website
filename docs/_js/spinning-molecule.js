const protein = window.location.search == "?protein"

const viewer = new Miew({
	container: document.getElementById("miew-container"),
	// load: "2g64",
	// https://github.com/epam/miew/blob/25fea24038de937cd142049ec77b27bc1866001a/packages/lib/src/settings.js`
	settings: {
		axes: false,
		fps: false,
		// camFar: 50,
		camDistance: protein ? 1 : 1.6,
		resolution: "high",
		zooming: false,
		autoRotationAxisFixed: false,
		fog: true,
		bg: { color: 0x343434 },

		// Settings we don't want:
		// bg: { color: 0xffffff, transparent: true }, // Transparent background creates ugly edges
		autoRotation: 0.05,
	},
})
if (viewer.init()) {
	// viewer.enableHotKeys(false)
	viewer.run()
}
if (protein) {
	viewer.load("2g64")
} else {
	const sdf = molecules[0]
	viewer.load(sdf, { sourceType: "immediate", fileType: "sdf" })
}
