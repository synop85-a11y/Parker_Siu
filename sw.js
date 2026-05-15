// Network-first 전략: 항상 최신 버전 받아옴, 오프라인일 때만 캐시 사용
// 개발 중에는 캐시 문제가 없도록 이렇게 동작

const CACHE_NAME = 'parker-siu-dev';

self.addEventListener('install', (e) => {
  // 새 버전 즉시 활성화
  self.skipWaiting();
});

self.addEventListener('activate', (e) => {
  // 모든 이전 캐시 삭제
  e.waitUntil(
    caches.keys().then((keys) => Promise.all(
      keys.map(k => caches.delete(k))
    )).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (e) => {
  // 항상 네트워크에서 최신 가져옴
  e.respondWith(
    fetch(e.request)
      .then((response) => {
        // 성공하면 백업으로 캐시에 저장
        if (response && response.status === 200) {
          const clone = response.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(e.request, clone));
        }
        return response;
      })
      .catch(() => {
        // 네트워크 실패하면 (오프라인) 캐시에서 가져옴
        return caches.match(e.request);
      })
  );
});
