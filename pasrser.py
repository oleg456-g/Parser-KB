from selenium import webdriver
from selenium.webdriver.common.by import By
import csv


def get_info():
    # Настраиваем браузер Chrome
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_argument("--disable-notifications")
    # Открываем страницу КБ
    driver = webdriver.Chrome(chrome_options=chrome_options)
    url = "https://krasnoeibeloe.ru/catalog/vino-s-otsenkoy/"
    driver.get(url)
    # Получаем информацию
    get_vines = driver.find_elements(By.CLASS_NAME, "catalog_product_item_cont")
    # driver.quit()

    for vine in get_vines:
        get_text_about_vine = vine.text.split('\n')
        process_text = [get_text_about_vine[2]] + get_text_about_vine[5:8]
        yield process_text

    return process_text


# Функция записи в файл csv
def main():
    text = get_info()
    with open('vine.csv', 'w', newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(['Баллы', 'Вино', 'Литраж, Страна', 'Цена'])
        for info_vine in text:
            print(info_vine)
            writer.writerow(info_vine)


if __name__ == '__main__':
    main()
