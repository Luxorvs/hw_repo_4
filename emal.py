import datetime
from pprint import pprint

# 1. Создайте словарь email, содержащий следующие поля:
# "subject" (тема письма), "from" (адрес отправителя), "to" (адрес получателя), "body" (текст письма).

email = {
    "subject": "Project collaboration",
    "from": " Partner@organization.org",
    "to": "Lead_dev@icloud.com ",
    "body": "Hello,\nWe are interested in a partnership.\tPlease reply soon.\nRegards,\nTeam",
}
print("Пункт 1. Исходник: ", email)

# 2. Добавьте дату отправки: создайте переменную send_date
# как текущую дату в формате YYYY-MM-DD и запишите её в email["date"].

send_date = datetime.datetime.now().strftime("%Y-%m-%d")
email["date"] = send_date
print(f"Пункт 2. Добавляем дату: ", email)

# 3. Нормализуйте e-mail адреса отправителя и получателя:
# приведите к нижнему регистру и уберите пробелы по краям.
# Запишите обратно в email["from"] и email["to"].

email["from"] = email["from"].strip().lower()
email["to"] = email["to"].strip().lower()
print(
    f"""Пункт 3. Правим адреса', 
        {email["from"]}, 
        {email["to"]}"""
)

# 4. Извлеките логин и домен отправителя в две переменные login и domain.

login = email["from"].split("@")[0]
domain = email["from"].split("@")[1]
print(
    f"""Пункт 4. Извлечение логина и домена отправителя.
        Логин: {login}
        Домен: {domain}"""
)

# 5.Создайте сокращённую версию текста: возьмите первые 10 символов email["body"]
# и добавьте многоточие "...". Сохраните в новый ключ словаря: email["short_body"].

email["short_body"] = email["body"][:10] + "..."
print(f'Пункт 5. Создаем сокращённую версию текста. {email["short_body"]}')

# 6. Списки доменов: создайте список личных доменов ['gmail.com','list.ru', 'yahoo.com','outlook.com',
# 'hotmail.com','icloud.com','yandex.ru','mail.ru','list.ru','bk.ru','inbox.ru']
# и список корпоративных доменов ['company.ru','corporation.com','university.edu','organization.org',
# 'company.ru', 'business.net']. с учетом того что там должны быть только уникальные значение

personal = [
    "gmail.com",
    "list.ru",
    "yahoo.com",
    "outlook.com",
    "hotmail.com",
    "icloud.com",
    "yandex.ru",
    "mail.ru",
    "list.ru",
    "bk.ru",
    "inbox.ru",
]
corporate = [
    "company.ru",
    "corporation.com",
    "university.edu",
    "organization.org",
    "company.ru",
    "business.net",
]

personal_domens = list(set(personal))
corporate_domens = list(set(corporate))
print(
    f"""Пункт 6. 
        Личные домены {personal_domens}
        Корпоративные домены: {corporate_domens}"""
)

# 7. Проверьте что в списке личных и корпоративных доменов нет пересечений: ни один домен не должен входить в оба списка одновременно.

check = set(personal_domens) & set(corporate_domens)
if check:
    print(f"Пункт 7. перечения : {check}")

# 8.Проверьте «корпоративность» отправителя:
# создайте булеву переменную is_corporate, равную результату проверки
# вхождения домена отправителя в список корпоративных доменов.

is_corporate = domain in corporate_domens
print(f"Пункт 8. Проверям «корпоративность» : {is_corporate}")

# 9.Соберите «чистый» текст сообщения без табов и переводов строк:
# замените "\t" и "\n" на пробел. Сохраните в email["clean_body"].
email["clean_body"] = email["body"].replace("\t", " ").replace("\n", " ")
print(f"Пункт 9. Чистый текст: {email['clean_body']}")

# 10.Сформируйте текст отправленного письма многострочной f-строкой и сохраните в email["sent_text"]:
# Кому: {получатель}, от {отправитель}
# Тема: {тема письма}, дата {дата} {чистый текст сообщения}
email[
    "sent_text"
] = f"""
    Кому: {email["to"]}, 
    От {email["from"]}
    Тема: {email["subject"]}
    Дата {send_date}
    {email["clean_body"]}"""

print(f'Пункт 10. Новое письмо: {email["sent_text"]}')

# 11. Рассчитайте количество страниц печати для email["sent_text"], если на 1 страницу помещается 500 символов.
# Сохраните результат в переменную pages. Значение должно быть округленно в большую сторону.

pages = (len(email["sent_text"]) + 499) // 500
print("Пункт 11. Количество страниц: ", pages)

# 12.Проверьте пустоту темы и тела письма:
# создайте переменные is_subject_empty, is_body_empty в котором будет хранится что тема письма содержит данные.

is_subject_empty = not email["subject"].strip()
is_body_empty = not email["body"].strip()
print(
    f"""Пункт 12.Проверяем пустоту темы и тела письма.
        Пустая тема письма: , {is_subject_empty})
        Пустое тело письма: , {is_body_empty}"""
)

# 13. Создайте «маску» e-mail отправителя: первые 2 символа логина + "***@" + домен.
# Запишите в email["masked_from"].
email["masked_from"] = login[:2] + "***@" + domain
print("Пункт 13. Создаеv «маску» e-mail отправителя", email["masked_from"])

# 14. Удалите из списка личных доменов значения "list.ru" и "bk.ru".
personal_domens.remove("list.ru")
personal_domens.remove("bk.ru")
print("Пункт 14. Чистим список личных доменов ", personal_domens)

# Итог
print(f"\n\nИтог:")
pprint(email)
