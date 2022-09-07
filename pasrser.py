from selenium import webdriver
from selenium.webdriver.common.by import By
import csv


def get_info(url):
    # Настраиваем браузер Chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")

    get_vines_name = []
    get_vines_price = []
    # Открываем страницу КБ и получаем количество страниц
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    pages = driver.find_elements(By.CLASS_NAME, "bl_pagination")
    # Да, можно было не писать следующие две строчки но так быстрее расботает
    get_vines_name += driver.find_elements(By.CLASS_NAME, "product_item_name")
    get_vines_price += driver.find_elements(By.CLASS_NAME, "product_item__price")

    for page in pages[0].text.split('\n')[:-1]:
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get(f"{url}?PAGEN_1={int(page)+1}")
        # Получаем информацию
        get_vines_name += driver.find_elements(By.CLASS_NAME, "product_item_name")
        get_vines_price += driver.find_elements(By.CLASS_NAME, "product_item__price")

    # Объединяем информацию из трёх переменных создаём генератор
    for i in range(len(get_vines_price)):
        yield [get_vines_name[i].text.replace('\n', ','), get_vines_price[i].text]


# Функция записи в файл csv
def main(url):
    text = get_info(url)
    # Открываем csv файл
    with open('vine.csv', 'w', newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(['Вино(описание)', 'Цена'])
        # Записываем в csv файл данные
        for info_vine in text:
            writer.writerow(info_vine)



if __name__ == '__main__':
    url = input('Вставьте ссылку на страницу --> ')
    # Проверка введенной ссылки
    if '://' not in url or 'krasnoeibeloe' not in url:
        print('\nВведите правильную ссылку!')
    else:
        main(url)
