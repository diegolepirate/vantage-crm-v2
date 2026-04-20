// Vantage Book — 3D asset cache (cache-first for .glb + 3D template HTML)
// Version bump to invalidate old cache on each deploy.
const CACHE_V = 'vantage-3d-v2';
const CACHE_TARGETS = [
  /\/assets\/models\/.*\.glb(\?|$)/,
  /vantage-maison-vitesse\.html/,
  /vantage-maison-luxe\.html/,
  /vantage-space-sweeper\.html/,
  /vantage-neoarcade\.html/,
  /vantage-hellenica\.html/,
  /vantage-tee-nou\.html/
];

self.addEventListener('install', e => {
  self.skipWaiting();
});

self.addEventListener('activate', e => {
  e.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.filter(k => k !== CACHE_V).map(k => caches.delete(k)));
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', e => {
  const url = e.request.url;
  // Only GET
  if (e.request.method !== 'GET') return;
  const match = CACHE_TARGETS.some(r => r.test(url));
  if (!match) return;
  e.respondWith((async () => {
    const cache = await caches.open(CACHE_V);
    const cached = await cache.match(e.request);
    if (cached) {
      // stale-while-revalidate for HTML; pure cache-first for .glb
      if (/\.html/.test(url)) {
        e.waitUntil(fetch(e.request).then(r => { if (r.ok) cache.put(e.request, r.clone()); }).catch(() => {}));
      }
      return cached;
    }
    try {
      const fresh = await fetch(e.request);
      if (fresh.ok) cache.put(e.request, fresh.clone());
      return fresh;
    } catch (err) {
      return new Response('', { status: 504 });
    }
  })());
});
