(() => {
  const endpointMeta = document.querySelector('meta[name="xioo-goatcounter-endpoint"]');
  const endpoint = endpointMeta ? endpointMeta.content.trim() : "";

  if (!endpoint) {
    return;
  }

  const goatCounterScript = document.createElement("script");
  goatCounterScript.async = true;
  goatCounterScript.src = "https://gc.zgo.at/count.js";
  goatCounterScript.dataset.goatcounter = endpoint;
  document.head.appendChild(goatCounterScript);
})();
