const BASE_URL = "https://trendmapper.onrender.com";

let totalChart, eventChart, productChart;

// TRACK EVENT
async function track(type, productId) {
  await fetch(`${BASE_URL}/track`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      event_type: type,
      product_id: productId
    })
  });

  loadData();
}

// LOAD DATA
async function loadData() {
  const res = await fetch(`${BASE_URL}/events`);
  const data = await res.json();

  let total = data.length;
  let view = 0, cart = 0;
  let products = {};

  data.forEach(e => {
    if (e.event_type === "view") view++;
    if (e.event_type === "add_to_cart") cart++;

    products[e.product_id] = (products[e.product_id] || 0) + 1;
  });

  if (totalChart) totalChart.destroy();
  totalChart = new Chart(document.getElementById("totalChart"), {
    type: "bar",
    data: { labels:["Total"], datasets:[{ data:[total] }] }
  });

  if (eventChart) eventChart.destroy();
  eventChart = new Chart(document.getElementById("eventChart"), {
    type: "pie",
    data: { labels:["View","Cart"], datasets:[{ data:[view,cart] }] }
  });

  if (productChart) productChart.destroy();
  productChart = new Chart(document.getElementById("productChart"), {
    type: "bar",
    data: {
      labels:Object.keys(products),
      datasets:[{ data:Object.values(products) }]
    }
  });

  generateAI(data);
}

// AI INSIGHT
function generateAI(data) {
  if (data.length === 0) {
    document.getElementById("aiOutput").innerHTML = "No data yet";
    return;
  }

  let count = {};
  data.forEach(e => {
    count[e.product_id] = (count[e.product_id] || 0) + 1;
  });

  let top = Object.keys(count).reduce((a,b)=> count[a]>count[b]?a:b);

  document.getElementById("aiOutput").innerHTML =
    `🔥 Most Popular Product: ${top}`;
}

window.onload = loadData;
