// Vantage Book — SW self-destruct build.
// Previous SW versions may have cached broken .glb responses from the short
// meshopt re-compression window, which caused 3D models to render blank.
// This version purges all caches and unregisters itself, so every client falls
// back to normal network fetches (no SW interception, no stale cache).
self.addEventListener('install', e => { self.skipWaiting(); });
self.addEventListener('activate', e => {
  e.waitUntil((async () => {
    try {
      const keys = await caches.keys();
      await Promise.all(keys.map(k => caches.delete(k)));
      await self.registration.unregister();
      const clients = await self.clients.matchAll({ includeUncontrolled: true });
      clients.forEach(c => c.navigate(c.url).catch(() => {}));
    } catch (e) {}
  })());
});
self.addEventListener('fetch', () => {}); // pass-through, no interception
