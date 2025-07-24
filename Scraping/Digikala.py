import requests
import csv

def fetch_incredible_products():
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) "
            "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
        )
    }
    base_url = "https://api.digikala.com/v1/incredible-offers/products/"
    params = {"has_selling_stock": 1, "q": None, "page": 1}

    csv_columns = ["image_url", "name", "text", "link", "shop_name", "old_price", "final_price", "discount", "timer"]
    items = []

    resp = requests.get(base_url, params=params, headers=headers)
    resp.raise_for_status()
    data = resp.json()

    total_pages = data["data"]["pager"]["total_pages"]

    for page in range(1, total_pages + 1):
        params["page"] = page
        resp = requests.get(base_url, params=params, headers=headers)
        resp.raise_for_status()
        data = resp.json()

        for item in data["data"]["products"]:
            resp2 = requests.get(f"https://api.digikala.com/v1/product/{item['id']}/seller-vouchers/", params={"productId" : item['id']}, headers=headers)
            resp2.raise_for_status()
            detail_data = resp2.json()
            print(detail_data)
            try:
                timer = item['default_variant']['price']['timer']
            except:
                try:
                    timer = item['second_default_variant']['price']['timer']
                except:
                    timer = None

            product = {
                "image_url" : item['images']['main']['url'][0],
                "name" : item['title_fa'] or item['title_en'],
                "text" : detail_data['data']['product']['description'],
                "link" : '/'.join(item['url']['uri'].split('/')[:3]) + item['title_fa'] or item['title_en'],
                "shop_name" : item['default_variant']['seller']['title'],
                "old_price" : item['default_variant']['price']['rrp_price'],
                "final_price" : item['default_variant']['price']['selling_price'],
                "discount" : item['default_variant']['price']['discount_percent'],
                "timer" : timer,
            }
            items.append(product)

    with open('digikala.csv', 'a', encoding='utf8') as DigikalaProducts:
        writer = csv.DictWriter(DigikalaProducts, fieldnames=csv_columns)
        writer.writeheader()
        for i in items:
            writer.writerow(i)
    return items

if __name__ == "__main__":
    products = fetch_incredible_products()
    print(f"➜ تعداد محصولات جمع‌آوری‌شده: {len(products)}")