import requests
import csv
import json
from collections import defaultdict
from PIL import Image, ImageDraw, ImageFont
from const import token,url,getClassName
# JWT tokeningizni shu yerga kiriting
jwt_token = token

# API URL manzili

# Headerlarni tayyorlash
headers = {
    "Authorization": f"{jwt_token}"
}

def getNot():
    try:
        # GET so'rov yuborish
        data = {"first":0,"rows":1000,"sortOrder":1,"filters":'{}',"globalFilter":'null'}
        response = requests.post(url, json=data, headers=headers,verify=False)
        response.raise_for_status()  # Xato bo'lsa, exception chiqaradi

        # JSON ma'lumotni olish
        data = response.json()

        # "data" kalitidan ma'lumotlarni olish
        student_data = data.get("users", [])

        grouped_data = defaultdict(list)
        for item in student_data:
            grouped_data[item["tbClassId"]].append(item)

        # Har bir tbClassId uchun CSV va jadval shaklida rasm yaratish
        for tbClassId, items in grouped_data.items():
            clasname = getClassName(tbClassId)
            filename = f"csv2/{clasname}.csv"
            with open(filename, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["F.I.SH", "login", "parol"])  # Ustun sarlavhalari
                for item in items:
                    writer.writerow([item["fullName"], item["login"], item["idNumberFull"]])
            print(f"Fayl yaratildi: {filename}")
            
            # Jadval shaklida rasm yaratish
            col_widths = [390, 300, 200]
            row_height = 40
            img_width = sum(col_widths) + 20
            img_height = (len(items) + 1) * row_height + 20
            img = Image.new("RGB", (img_width, img_height), "white")
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype("arialbd.ttf", 15)
            
            # Sarlavhalarni chizish
            headers2 = ["F.I.SH", "login", "parol"]
            x_offset = 10
            y_offset = 10
            for i, header in enumerate(headers2):
                draw.text((x_offset, y_offset), header, fill="black", font=font)
                x_offset += col_widths[i]
            y_offset += row_height
            
            # Jadval ma'lumotlarini chizish
            for item in items:
                x_offset = 10
                row_data = [item['fullName'], item['login'], item['idNumberFull']]
                for i, data in enumerate(row_data):
                    draw.text((x_offset, y_offset), data, fill="black", font=font)
                    x_offset += col_widths[i]
                y_offset += row_height
            
            # Rasmni saqlash
            img.save(f"img/{clasname}.png")
            print(f"Jadval shaklida rasm yaratildi: class_{tbClassId}.png")


    except requests.exceptions.RequestException as e:
        print(f"So'rov xatosi: {e}")
    except Exception as e:
        print(f"Xato yuz berdi: {e}")
getNot()