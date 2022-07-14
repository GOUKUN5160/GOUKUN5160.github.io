var CACHE_NAME = 'static-v2';
var urlsToCache = [
    '/bigtag/js/main.js',
];

// インストール処理
self.addEventListener('install', function(event) {
    console.log("install");
    event.waitUntil(
        caches
            .open(CACHE_NAME)
            .then(function(cache) {
                return cache.addAll(urlsToCache);
            })
    );
});

self.addEventListener('activate', () => {
    console.log('activate');
    e.waitUntil(self.clients.claim());
});

// リソースフェッチ時のキャッシュロード処理
self.addEventListener('fetch', function(event) {
    event.respondWith(
        caches
            .match(event.request)
            .then(function(response) {
                return response || fetch(event.request);
            })
    );
});