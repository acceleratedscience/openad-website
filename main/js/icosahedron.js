// Scene setup
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x333333);

//   // Camera
//   const camera = new THREE.PerspectiveCamera(
//     75,
//     window.innerWidth / window.innerHeight,
//     0.1,
//     1000
//   );
//   camera.position.z = 5;

// #region

const aspect = window.innerWidth / window.innerHeight;
const viewSize = 10; // Controls how much of the scene is visible
console.log(-viewSize * aspect, viewSize * aspect, viewSize, -viewSize);
const camera = new THREE.OrthographicCamera(
  -viewSize * aspect,
  viewSize * aspect,
  viewSize,
  -viewSize,
  0.1,
  1000
);

// Position for isometric view
// These specific values create the isometric angle
camera.position.set(1, 1, 1);
camera.lookAt(0, 0, 0);

// Optional: Normalize the direction vector to ensure true isometric angles
camera.position.normalize();
camera.position.multiplyScalar(15); // Distance from origin

// #endregion

// Renderer
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Icosahedron
const geometry = new THREE.IcosahedronGeometry(2, 0);
const material = new THREE.MeshPhongMaterial({
  color: 0xffffff,
  shininess: 100,
  specular: 0x111111,
});
const icosahedron = new THREE.Mesh(geometry, material);
scene.add(icosahedron);

// Lighting
const ambientLight = new THREE.AmbientLight(0x363636);
scene.add(ambientLight);

const directionalLight = new THREE.DirectionalLight(0xffffff, 0.5);
directionalLight.position.set(-1, 1, 1);
// directionalLight.position.set(0, 0, 1);
scene.add(directionalLight);

// Three rotation vectors
const rotationVectors = {
  xAxis: new THREE.Vector3(1, 0, 0), // For up/down movement
  yAxis: new THREE.Vector3(0, 1, 0), // For left/right movement
  zAxis: new THREE.Vector3(0, 0, 1), // Unused in this implementation
};

// Mouse state
let isMouseDown = false;
let previousMousePosition = { x: 0, y: 0 };
const ROTATION_SENSITIVITY = 0.01;

// Auto rotation
let autoRotateAxis = new THREE.Vector3(
  Math.random() - 0.5,
  Math.random() - 0.5,
  Math.random() - 0.5
).normalize();
const AUTO_ROTATION_SPEED = 0.005;
let lastInteractionTime = 0;

// Mouse event handlers
function onMouseDown(event) {
  isMouseDown = true;
  previousMousePosition = {
    x: event.clientX,
    y: event.clientY,
  };
}

function onMouseMove(event) {
  if (!isMouseDown) return;

  const deltaMove = {
    x: event.clientX - previousMousePosition.x,
    y: event.clientY - previousMousePosition.y,
  };

  // Simplified rotation based on mouse movement
  if (Math.abs(deltaMove.x) > Math.abs(deltaMove.y)) {
    // Handle horizontal movement
    if (deltaMove.x > 0) {
      // Moving right, rotate around Y axis (upward)
      icosahedron.rotateOnAxis(
        rotationVectors.yAxis,
        ROTATION_SENSITIVITY * deltaMove.x
      );
      autoRotateAxis = rotationVectors.yAxis.clone();
    } else {
      // Moving left, rotate around Y axis (downward)
      icosahedron.rotateOnAxis(
        rotationVectors.yAxis,
        ROTATION_SENSITIVITY * deltaMove.x
      );
      autoRotateAxis = rotationVectors.yAxis.clone().negate();
    }
  } else {
    // Handle vertical movement
    if (deltaMove.y > 0) {
      // Moving down, rotate around X axis (downward)
      icosahedron.rotateOnAxis(
        rotationVectors.xAxis,
        ROTATION_SENSITIVITY * -deltaMove.y
      );
      autoRotateAxis = rotationVectors.xAxis.clone().negate();
    } else {
      // Moving up, rotate around X axis (upward)
      icosahedron.rotateOnAxis(
        rotationVectors.xAxis,
        ROTATION_SENSITIVITY * -deltaMove.y
      );
      autoRotateAxis = rotationVectors.xAxis.clone();
    }
  }

  previousMousePosition = {
    x: event.clientX,
    y: event.clientY,
  };

  lastInteractionTime = Date.now();
}

function onMouseUp() {
  isMouseDown = false;
}

// Event listeners
document.addEventListener("mousedown", onMouseDown, false);
document.addEventListener("mousemove", onMouseMove, false);
document.addEventListener("mouseup", onMouseUp, false);

// Animation loop
function animate() {
  requestAnimationFrame(animate);

  // Auto rotation if not currently interacting
  if (!isMouseDown && Date.now() - lastInteractionTime > 100) {
    icosahedron.rotateOnAxis(autoRotateAxis, AUTO_ROTATION_SPEED);
  }

  // Render
  renderer.render(scene, camera);
}

// Responsive resize
window.addEventListener("resize", () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});

// Start animation
animate();
