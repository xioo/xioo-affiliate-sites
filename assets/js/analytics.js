(() => {
  const placeholderToken = "CLOUDFLARE_WEB_ANALYTICS_TOKEN";
  const tokenMeta = document.querySelector('meta[name="xioo-cloudflare-web-analytics-token"]');
  const token = tokenMeta ? tokenMeta.content.trim() : "";

  if (!token || token === placeholderToken) {
    return;
  }

  const beaconScript = document.createElement("script");
  beaconScript.defer = true;
  beaconScript.src = "https://static.cloudflareinsights.com/beacon.min.js";
  beaconScript.dataset.cfBeacon = JSON.stringify({ token });
  document.head.appendChild(beaconScript);
})();
