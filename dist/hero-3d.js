import * as THREE from './assets/js/three.module.js';

const poster = document.querySelector('.portrait-poster');
const studio = document.querySelector('.studio-main');
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

if (poster && !reducedMotion.matches) {
  try {
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(38, 1, 0.1, 100);
    camera.position.z = 5.4;
    const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true, powerPreference: 'low-power' });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.7));
    renderer.setClearColor(0x000000, 0);
    renderer.domElement.className = 'poster-canvas';
    renderer.domElement.setAttribute('aria-hidden', 'true');
    poster.prepend(renderer.domElement);

    const geometry = new THREE.IcosahedronGeometry(1.62, 2);
    const material = new THREE.MeshBasicMaterial({ color: 0x183b31, wireframe: true, transparent: true, opacity: 0.4 });
    const form = new THREE.Mesh(geometry, material);
    scene.add(form);

    let targetX = 0;
    let targetY = 0;
    let frame = 0;
    const resize = () => {
      const { width, height } = poster.getBoundingClientRect();
      camera.aspect = width / height;
      camera.updateProjectionMatrix();
      renderer.setSize(width, height, false);
    };
    const observer = new ResizeObserver(resize);
    observer.observe(poster);
    poster.addEventListener('pointermove', (event) => {
      const bounds = poster.getBoundingClientRect();
      targetX = ((event.clientY - bounds.top) / bounds.height - 0.5) * 0.55;
      targetY = ((event.clientX - bounds.left) / bounds.width - 0.5) * 0.55;
    }, { passive: true });
    poster.addEventListener('pointerleave', () => { targetX = 0; targetY = 0; });
    const render = () => {
      if (document.hidden || !poster.isConnected) {
        frame = requestAnimationFrame(render);
        return;
      }
      form.rotation.x += (targetX - form.rotation.x) * 0.025;
      form.rotation.y += (targetY - form.rotation.y) * 0.025;
      form.rotation.z += 0.0008;
      renderer.render(scene, camera);
      frame = requestAnimationFrame(render);
    };
    resize();
    render();
    window.addEventListener('pagehide', () => {
      cancelAnimationFrame(frame);
      observer.disconnect();
      geometry.dispose();
      material.dispose();
      renderer.dispose();
    }, { once: true });
  } catch {
    // The CSS artwork remains visible on devices without WebGL.
  }
}

if (studio && !reducedMotion.matches) {
  try {
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(40, 1, .1, 100);
    camera.position.z = 5.5;
    const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true, powerPreference: 'low-power' });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.5));
    renderer.domElement.className = 'studio-canvas';
    renderer.domElement.setAttribute('aria-hidden', 'true');
    studio.append(renderer.domElement);
    const geometry = new THREE.TorusKnotGeometry(1.05, .27, 130, 8, 2, 3);
    const material = new THREE.MeshBasicMaterial({ color: 0x294636, wireframe: true, transparent: true, opacity: .55 });
    const knot = new THREE.Mesh(geometry, material);
    scene.add(knot);
    let frame = 0;
    const resize = () => renderer.setSize(renderer.domElement.clientWidth, renderer.domElement.clientHeight, false);
    const observer = new ResizeObserver(resize);
    observer.observe(renderer.domElement);
    const render = () => {
      if (document.hidden) { frame = requestAnimationFrame(render); return; }
      knot.rotation.x += .0012;
      knot.rotation.y += .0018;
      renderer.render(scene, camera);
      frame = requestAnimationFrame(render);
    };
    resize();
    render();
    window.addEventListener('pagehide', () => { cancelAnimationFrame(frame); observer.disconnect(); geometry.dispose(); material.dispose(); renderer.dispose(); }, { once: true });
  } catch {
    // Static studio typography remains available without WebGL.
  }
}
