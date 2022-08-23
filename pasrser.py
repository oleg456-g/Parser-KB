from selenium import webdriver
from selenium.webdriver.common.by import By
import csv


def get_info():
    # Настраиваем браузер Chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    # Открываем страницу КБ
    driver = webdriver.Chrome(chrome_options=chrome_options)
    url = "https://krasnoeibeloe.ru/catalog/vino-s-otsenkoy/"
    driver.get(url)
    # Получаем информацию
    get_vines_name = driver.find_elements(By.CLASS_NAME, "product_item_name")
    get_vines_price = driver.find_elements(By.CLASS_NAME, "product_item__price")
    get_vines_rating = driver.find_elements(By.CLASS_NAME, "bl_rob_p__rating")

    for i in range(len(get_vines_name)):
        yield [get_vines_rating[i].text, get_vines_name[i].text.replace('\n', ' '), get_vines_price[i].text]


# Функция записи в файл csv
def main():
    text = get_info()
    with open('vine.csv', 'w', newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(['Баллы', 'Вино', 'Цена'])
        for info_vine in text:
            print(info_vine)
            writer.writerow(info_vine)


if __name__ == '__main__':
    main()
