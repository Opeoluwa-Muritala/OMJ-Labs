import * as THREE from './assets/js/three.module.js';

const loader = document.querySelector('.site-loader');
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (loader) {
  if (reduceMotion) {
    loader.remove();
  } else {
    let stopScene = () => {};
    const art = loader.querySelector('.loader-art');
    try {
      const scene = new THREE.Scene();
      const camera = new THREE.PerspectiveCamera(38, 1, .1, 100);
      camera.position.z = 6;
      const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true, powerPreference: 'low-power' });
      renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.5));
      renderer.setSize(230, 230, false);
      renderer.domElement.className = 'loader-canvas';
      renderer.domElement.setAttribute('aria-hidden', 'true');
      art.prepend(renderer.domElement);
      const ring = new THREE.Mesh(
        new THREE.TorusGeometry(1.75, .065, 12, 100),
        new THREE.MeshBasicMaterial({ color: 0xd5ef82, transparent: true, opacity: .85 })
      );
      const smallerRing = new THREE.Mesh(
        new THREE.TorusGeometry(1.28, .025, 8, 88),
        new THREE.MeshBasicMaterial({ color: 0xf5f5ed, transparent: true, opacity: .3 })
      );
      ring.rotation.x = .5;
      smallerRing.rotation.y = .8;
      scene.add(ring, smallerRing);
      let frame = 0;
      const render = () => {
        ring.rotation.y += .02;
        ring.rotation.z += .005;
        smallerRing.rotation.x -= .014;
        renderer.render(scene, camera);
        frame = requestAnimationFrame(render);
      };
      render();
      stopScene = () => {
        cancelAnimationFrame(frame);
        ring.geometry.dispose();
        ring.material.dispose();
        smallerRing.geometry.dispose();
        smallerRing.material.dispose();
        renderer.dispose();
      };
    } catch {
      // The logo and CSS ring remain visible without WebGL.
    }
    const close = () => {
      loader.classList.add('is-done');
      stopScene();
      window.setTimeout(() => loader.remove(), 400);
    };
    window.setTimeout(close, 850);
  }
}
