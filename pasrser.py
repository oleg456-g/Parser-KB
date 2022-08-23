from selenium import webdriver
from selenium.webdriver.common.by import By
import csv


def get_info():
    # Настраиваем браузер Chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")

    get_vines_name = []
    get_vines_price = []
    get_vines_rating = []
    page_count = input('Введите количество страниц в разделе --> ')
    if page_count.isdigit():
        for a in range(int(page_count)):
            # Открываем страницу КБ
            driver = webdriver.Chrome(chrome_options=chrome_options)
            url = f"https://krasnoeibeloe.ru/catalog/vino-s-otsenkoy/?PAGEN_1={a+1}"
            # Получаем информацию
            driver.get(url)
            get_vines_name += driver.find_elements(By.CLASS_NAME, "product_item_name")
            get_vines_price += driver.find_elements(By.CLASS_NAME, "product_item__price")
            get_vines_rating += driver.find_elements(By.CLASS_NAME, "bl_rob_p__rating")
        # Объединяем информацию из трёх переменных создаём генератор
        for i in range(len(get_vines_price)):
            yield [get_vines_rating[i].text, get_vines_name[i].text.replace('\n', ','), get_vines_price[i].text]
    else:
        print('Убедитесь, что ввели только цифры!')


# Функция записи в файл csv
def main():
    text = get_info()
    with open('vine.csv', 'w', newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(['Баллы', 'Вино(описание)', 'Цена'])
        # Записываем в csv файл данные
        for info_vine in text:
            writer.writerow(info_vine)


if __name__ == '__main__':
    main()
