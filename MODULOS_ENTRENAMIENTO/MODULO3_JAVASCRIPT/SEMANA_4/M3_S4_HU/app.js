// ================================
// CRUDTECH - APP
// ================================

// ===== API =====
const API_URL = "http://localhost:3000/products";

// ===== DOM =====
const form = document.getElementById("product-form");
const productList = document.getElementById("product-list");
const syncButton = document.getElementById("sync-api");

const nameInput = document.getElementById("product-name");
const categoryInput = document.getElementById("product-category");
const brandInput = document.getElementById("product-brand");
const priceInput = document.getElementById("product-price");
const stockInput = document.getElementById("product-stock");

// ===== ESTADO =====
let products = [];

// ================================
// EVENTOS
// ================================
form.addEventListener("submit", handleAddProduct);
syncButton.addEventListener("click", getProductsFromAPI);

// ================================
// INICIALIZACIÓN
// ================================
document.addEventListener("DOMContentLoaded", () => {
  console.log("📦 App iniciada");

  const storedProducts = localStorage.getItem("products");

  if (storedProducts) {
    products = JSON.parse(storedProducts);
    products.forEach(product => renderProduct(product));
  }
});

// ================================
// FUNCIONES
// ================================
function handleAddProduct(event) {
  event.preventDefault();

  const name = nameInput.value.trim();
  const category = categoryInput.value.trim();
  const brand = brandInput.value.trim();
  const price = Number(priceInput.value);
  const stock = Number(stockInput.value);

  if (!name || !category || !brand || price <= 0 || stock < 0) {
    alert("Todos los campos son obligatorios");
    return;
  }

  const product = { name, category, brand, price, stock };
  postProductToAPI(product);

  form.reset();
}

// ================================
// RENDER DOM
// ================================
function renderProduct(product) {
  const li = document.createElement("li");
  li.className =
    "bg-white p-4 rounded shadow flex justify-between items-center";

  li.innerHTML = `
    <div>
      <p class="font-bold">${product.name}</p>
      <p class="text-sm text-gray-600">${product.brand} | ${product.category}</p>
      <p class="text-sm">💲${product.price} | Stock: ${product.stock}</p>
    </div>
  `;

  const deleteButton = document.createElement("button");
  deleteButton.textContent = "Eliminar";
  deleteButton.className =
    "bg-red-500 text-white px-3 py-1 rounded hover:bg-red-600";

  deleteButton.addEventListener("click", () =>
    deleteProductFromAPI(product.id, li)
  );

  li.appendChild(deleteButton);
  productList.appendChild(li);
}

// ================================
// FETCH API + LOGS PERSISTENTES
// ================================
async function getProductsFromAPI() {
  try {
    const response = await fetch(API_URL);
    const data = await response.json();

    console.group("📥 GET API");
    console.log("Productos obtenidos:", data);
    console.groupEnd();

    products = data;
    localStorage.setItem("products", JSON.stringify(products));

    productList.innerHTML = "";
    products.forEach(product => renderProduct(product));

  } catch (error) {
    console.error("❌ GET API error:", error.message);
  }
}

async function postProductToAPI(product) {
  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(product)
    });

    const newProduct = await response.json();

    console.group("📤 POST API");
    console.log("Producto creado:", newProduct);
    console.groupEnd();

    products.push(newProduct);
    localStorage.setItem("products", JSON.stringify(products));
    renderProduct(newProduct);

  } catch (error) {
    console.error("❌ POST API error:", error.message);
  }
}

async function deleteProductFromAPI(id, li) {
  try {
    await fetch(`${API_URL}/${id}`, { method: "DELETE" });

    console.group("🗑️ DELETE API");
    console.log(`Producto eliminado con id: ${id}`);
    console.groupEnd();

    products = products.filter(p => p.id !== id);
    localStorage.setItem("products", JSON.stringify(products));
    productList.removeChild(li);

  } catch (error) {
    console.error("❌ DELETE API error:", error.message);
  }
}
