/* ═══════════════════════════════════════════════════════════════
   APEX CONSULTING — SERVICE WORKER
   Cache First for assets · Network First for pages
   Background Sync for forms
═══════════════════════════════════════════════════════════════ */

const SW_VERSION   = 'apex-v1.0.0';
const CACHE_STATIC = SW_VERSION + '-static';
const CACHE_PAGES  = SW_VERSION + '-pages';
const CACHE_IMGS   = SW_VERSION + '-images';
const SYNC_TAG     = 'apex-form-sync';

const PRECACHE_ASSETS = [
  '/',
  '/index.html',
  '/offline.html',
];

/* INSTALL */
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_STATIC)
      .then(cache => cache.addAll(PRECACHE_ASSETS))
      .then(() => self.skipWaiting())
  );
});

/* ACTIVATE */
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(
        keys
          .filter(key => key.startsWith('apex-') && key !== CACHE_STATIC &&
                         key !== CACHE_PAGES && key !== CACHE_IMGS)
          .map(key => caches.delete(key))
      ))
      .then(() => self.clients.claim())
  );
});

/* FETCH */
self.addEventListener('fetch', event => {
  const { request } = event;
  const url = new URL(request.url);

  if (request.method !== 'GET') return;
  if (url.hostname !== self.location.hostname &&
      !url.hostname.includes('fonts.googleapis.com') &&
      !url.hostname.includes('fonts.gstatic.com') &&
      !url.hostname.includes('images.unsplash.com')) return;

  if (request.destination === 'image' ||
      url.hostname.includes('images.unsplash.com')) {
    event.respondWith(cacheFirst(request, CACHE_IMGS));
    return;
  }

  if (url.hostname.includes('fonts.googleapis.com') ||
      url.hostname.includes('fonts.gstatic.com')) {
    event.respondWith(cacheFirst(request, CACHE_STATIC));
    return;
  }

  if (request.headers.get('Accept')?.includes('text/html')) {
    event.respondWith(networkFirstWithOffline(request));
    return;
  }

  if (request.destination === 'script' ||
      request.destination === 'style') {
    event.respondWith(staleWhileRevalidate(request, CACHE_STATIC));
    return;
  }
});

/* BACKGROUND SYNC */
self.addEventListener('sync', event => {
  if (event.tag === SYNC_TAG) {
    event.waitUntil(syncFormData());
  }
});

async function syncFormData() {
  try {
    const db    = await openDB();
    const tx    = db.transaction('pending_forms', 'readwrite');
    const store = tx.objectStore('pending_forms');
    const forms = await getAllFromStore(store);

    for (const form of forms) {
      try {
        const response = await fetch('/api/contact', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(form.data),
        });
        if (response.ok) {
          await store.delete(form.id);
        }
      } catch(e) {
        console.warn('[SW] Form sync failed, will retry:', e);
      }
    }
  } catch(e) {
    console.warn('[SW] Background sync error:', e);
  }
}

/* PUSH NOTIFICATIONS */
self.addEventListener('push', event => {
  if (!event.data) return;
  const data = event.data.json();
  event.waitUntil(
    self.registration.showNotification(data.title || 'Apex Consulting', {
      body: data.body || 'You have a new message.',
      icon: data.icon || '/icons/icon-192.png',
      badge: data.badge || '/icons/badge-72.png',
      tag: data.tag || 'apex-notification',
      data: data.url ? { url: data.url } : {},
      actions: [
        { action: 'view',    title: 'View'    },
        { action: 'dismiss', title: 'Dismiss' },
      ],
      vibrate: [200, 100, 200],
    })
  );
});

self.addEventListener('notificationclick', event => {
  event.notification.close();
  if (event.action === 'view' || !event.action) {
    const url = event.notification.data?.url || '/';
    event.waitUntil(
      clients.matchAll({ type: 'window' }).then(windowClients => {
        const client = windowClients.find(c => c.url === url && 'focus' in c);
        if (client) return client.focus();
        if (clients.openWindow) return clients.openWindow(url);
      })
    );
  }
});

/* CACHE STRATEGIES */
async function cacheFirst(request, cacheName) {
  const cache  = await caches.open(cacheName);
  const cached = await cache.match(request);
  if (cached) return cached;
  try {
    const response = await fetch(request);
    if (response.ok) cache.put(request, response.clone());
    return response;
  } catch {
    return new Response('Resource unavailable offline.', { status: 503 });
  }
}

async function networkFirstWithOffline(request) {
  try {
    const response = await fetch(request);
    if (response.ok) {
      const cache = await caches.open(CACHE_PAGES);
      cache.put(request, response.clone());
    }
    return response;
  } catch {
    const cache  = await caches.open(CACHE_PAGES);
    const cached = await cache.match(request);
    if (cached) return cached;
    const offlineCache = await caches.open(CACHE_STATIC);
    const offline      = await offlineCache.match('/offline.html');
    return offline || new Response('<h1>You are offline</h1>', {
      headers: { 'Content-Type': 'text/html' },
    });
  }
}

async function staleWhileRevalidate(request, cacheName) {
  const cache  = await caches.open(cacheName);
  const cached = await cache.match(request);
  const networkFetch = fetch(request)
    .then(response => {
      if (response.ok) cache.put(request, response.clone());
      return response;
    })
    .catch(() => null);
  return cached || networkFetch;
}

/* INDEXEDDB HELPERS */
function openDB() {
  return new Promise((resolve, reject) => {
    const req = indexedDB.open('apex-sw-db', 1);
    req.onupgradeneeded = e => {
      e.target.result.createObjectStore('pending_forms', { keyPath: 'id', autoIncrement: true });
    };
    req.onsuccess = e => resolve(e.target.result);
    req.onerror   = e => reject(e.target.error);
  });
}

function getAllFromStore(store) {
  return new Promise((resolve, reject) => {
    const req = store.getAll();
    req.onsuccess = e => resolve(e.target.result);
    req.onerror   = e => reject(e.target.error);
  });
}
