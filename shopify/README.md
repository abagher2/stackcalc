# StackCalc Shopify E-Commerce Integration & Setup Guide

This directory contains the full product catalog, CSV import data, and integration specifications for the **StackCalc** Shopify storefront (`shop.stackcalc.io`).

---

## 📁 Directory Structure

| File | Purpose |
|---|---|
| [`shopify_products_import.csv`](shopify_products_import.csv) | Official Shopify Product CSV containing all 6 products, variants, pricing, inventory counts, weights, tags, and HTML descriptions. Ready for 1-click import into Shopify Admin. |
| [`products.json`](products.json) | Programmatic JSON schema of the catalog for headless storefronts, custom scripts, or API integrations. |
| [`01_sc32_founders_edition.md`](01_sc32_founders_edition.md) | Full specifications for SC-32 Founder's Edition ($89 USD, Batch 00, custom laser engraving). |
| [`02_sc32_regular_edition.md`](02_sc32_regular_edition.md) | Full specifications for SC-32 RPN Scientific Calculator ($59 USD, regular production). |
| [`03_sc6_elementary_edition.md`](03_sc6_elementary_edition.md) | Full specifications for SC-6 Elementary Math Calculator ($35 USD, Grades K–6 STEM). |
| [`04_unit_circle_volvelle.md`](04_unit_circle_volvelle.md) | Full specifications for The Unit Circle Volvelle ($18 USD, mechanical trigonometry tool). |
| [`05_reference_decks.md`](05_reference_decks.md) | Full specifications for StackCalc Reference Decks ($15 USD / set). |
| [`06_student_essentials_bundle.md`](06_student_essentials_bundle.md) | Full specifications for Student Essentials Bundle ($125 USD). |

---

## 🚀 Step 1: Importing Products into Shopify Admin

1. Log into your **Shopify Admin** (`https://admin.shopify.com/store/YOUR-STORE-NAME`).
2. Navigate to **Products** in the left sidebar.
3. Click the **Import** button in the top-right corner.
4. Select `shopify_products_import.csv` from this directory.
5. Check **"Overwrite any current products that have the same handle"** if re-importing updates.
6. Click **Upload and preview**, then click **Import products**.
### ⚠️ Troubleshooting Common Import Errors

#### 1. "Product Category or Product Type is Invalid"
* **The Root Cause:** Shopify separates **Product category** (strictly validated against Shopify's Standard Product Taxonomy) from **Type** (free-form custom label). If the CSV has an outdated or partial category string (like `Office Supplies > Calculators` instead of the full taxonomy `Business & Industrial > Office Supplies > Office Equipment > Calculators`), Shopify halts the import.
* **The Solution:** In `shopify_products_import.csv`, `Product category` is intentionally left empty (`""`). Shopify's import engine automatically determines and suggests the category based on the product Title and Description, completely bypassing taxonomy mismatch rejections.
* **Alternative:** If you want explicit taxonomy, use `shopify_products_import_with_taxonomy.csv`, which contains the exact full Shopify taxonomy string.

---

## 🖼️ Step 2: Adding Product Images (Two Approaches)

Because Shopify's CSV importer runs in the cloud, the `Product image URL` column requires a **public internet URL** (it cannot access local file paths on your computer). You have two ways to add images:

### Approach A: Drag-and-Drop in Shopify Admin (Recommended & Fastest)
1. Import `shopify_products_import.csv` with empty image URLs. All 6 products, 25 variants, SKUs, inventory, and descriptions will be created instantly.
2. In Shopify Admin, click **Products** -> click a product (e.g. *StackCalc SC-32 Founder's Edition*).
3. Scroll down to the **Media** section.
4. Drag and drop your product renders/photos directly from your computer into the Media box (or click **Add media**).
5. Click **Save**.

### Approach B: Upload to Shopify Files CDN (For Automated CSV Imports)
1. In Shopify Admin, click **Content > Files** in the left navigation.
2. Click **Upload files** and select your photos/renderings.
3. Once uploaded, click the **Link icon** next to each file to copy its CDN URL (`https://cdn.shopify.com/s/files/...`).
4. Paste the URL into the `Product image URL` column of `shopify_products_import.csv` on the row for that product.
5. Re-import the CSV. Shopify will download the images directly from its own CDN.

#### Ready-to-Use Image Assets in this Workspace:
* Angled 3D Hardware View: `docs/assets/isometric.png`
* Top-Down Keypad & Screen View: `docs/assets/topdown.png`
* Hero Banner: `docs/assets/hero.jpg`

---

## ✍️ Step 3: Custom Nameplate Engraving Setup (Founder's Edition)

For the **SC-32 Founder's Edition**, customer name engraving is captured via Shopify Line-Item Properties.

### Shopify Theme Setup (Liquid / Online Store 2.0):
In your theme editor, open the Product template for `sc32-founders-edition` and add a Custom Liquid block:

```html
<div class="line-item-property__field" style="margin: 1.5rem 0;">
  <label for="engraving" style="display: block; font-family: monospace; font-weight: bold; margin-bottom: 0.5rem;">
    // CUSTOM NAMEPLATE ENGRAVING (MAX 15 CHARS):
  </label>
  <input 
    type="text" 
    id="engraving" 
    name="properties[Engraving]" 
    maxlength="15" 
    placeholder="e.g. A. LOVELACE" 
    style="width: 100%; max-width: 400px; padding: 0.75rem; font-family: monospace; border: 2px solid #181A1B; text-transform: uppercase;"
  >
  <p style="font-size: 0.75rem; color: #666; margin-top: 0.25rem;">
    Laser engraved onto the rear plate in Space Mono font. Leave blank for standard serialized plate.
  </p>
</div>
```

The captured string will automatically appear in Shopify Admin under **Order Details > Custom Information**.

---

## 🛒 Step 4: Shopify Buy Button Integration

To link the products to the custom website (`https://stackcalc.io`):
1. In Shopify Admin, install the **Buy Button** sales channel.
2. Select **Create a Buy Button > Product Buy Button**.
3. Choose the product (e.g. `StackCalc SC-32 Founder's Edition`).
4. Set Action on click to: **Direct to checkout**.
5. Copy the generated Variant ID and map it to the corresponding button in `overrides/home.html`:
   - Founder's Edition (Live): `https://z4cvet-ig.myshopify.com/products/sc32-founders-edition`
   - SC-32 Regular (Planned): `https://shop.stackcalc.io/cart/add?id=kit-sc32`
   - SC-6 Elementary (Planned): `https://shop.stackcalc.io/cart/add?id=sc6-basic`
   - Unit Circle Volvelle (Planned): `https://shop.stackcalc.io/cart/add?id=unit-circle-volvelle`
   - Reference Decks (Planned): `https://shop.stackcalc.io/cart/add?id=refdeck-set1`

---

## 📦 Step 5: Shipping & Fulfillment Configuration

### Package Profiles:
- **Small Mailer (Accessories / Reference Decks):** 7 × 5 × 1 in, weight: ~0.2 lb
- **Calculator Box (SC-32 / SC-6 / Founder's Edition):** 6.6 × 4.9 × 1.9 in, weight: ~0.6 lb (converts into dual desk stands)
- **Bundle Box (Student Essentials):** 8 × 6 × 3 in, weight: ~0.9 lb

### HS Tariff Classification:
- **Calculators (`SC-32`, `SC-6`):** `8470.10.00`
- **Trig Volvelle:** `9017.20.80`
- **Reference Decks:** `4911.99.80`
