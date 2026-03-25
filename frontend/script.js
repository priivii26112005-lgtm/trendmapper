const BASE_URL = "https://trendmapper.onrender.com";

// TRACK EVENT
async function track(type, productId) {
  await fetch(`${BASE_URL}/track`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      user_id: "user1",
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

  // TOTAL CHART
  new Chart(document.getElementById("totalChart"), {
    type: "bar",
    data: {
      labels:["Total"],
      datasets:[{ data:[total] }]
    }
  });

  // EVENT CHART
  new Chart(document.getElementById("eventChart"), {
    type: "pie",
    data: {
      labels:["View","Cart"],
      datasets:[{ data:[view,cart] }]
    }
  });

  // PRODUCT CHART
  new Chart(document.getElementById("productChart"), {
    type: "bar",
    data: {
      labels:Object.keys(products),
      datasets:[{ data:Object.values(products) }]
    }
  });

  generateAI(data);
}

// AI FUNCTION
function generateAI(data) {
  let productCount = {};

  data.forEach(e => {
    productCount[e.product_id] = (productCount[e.product_id] || 0) + 1;
  });

  let topProduct = Object.keys(productCount).reduce((a, b) =>
    productCount[a] > productCount[b] ? a : b
  );

  document.getElementById("aiOutput").innerHTML =
    `🔥 Most Popular Product: ${topProduct} <br> 💡 Promote this product more!`;
}

// LOAD ON START
window.onload = loadData;