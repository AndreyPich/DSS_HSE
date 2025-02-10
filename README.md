# Лабораторная работа №0
## Тема
Система оповещения о чрезвычайных ситуациях
## Функциональные требования
Ввод чрезвычайных ситуаций:
1. Возможность ввода информации о возникшей чрезвычайной ситуации (тип, время, степень опасности, рекомендации).

Оповещение пользователей:
1. Рассылка уведомлений через различные каналы (SMS, Email, звонки).
2. Группировка получателей по местоположению.
   
Управление системой:
1. Управления настройками системы (каналы оповещения, получатели, расписание).
2. Отчёты и статистика (количество оповещений, время доставки).

## Модель предметной области
### Use case:
![image](https://github.com/user-attachments/assets/a18fd5eb-1c60-40bd-9bd0-8e0369e53eb5)
## DDD
Красное - Агрегаты, Зеленое - сущности, Синее - value object
![image](https://github.com/user-attachments/assets/6927e213-7ef8-4ef9-8281-8424fdebd490)

Глоссарий:
1. Operator - управляет системой оповещений.
2. EmergencyNotification - управляет уведомлениями о чрезвычайных ситуациях и связанными с ними сообщениями.
3. EmergencyEvent - управляет данными о чрезвычайных ситуациях.
4. Recipient - управляет получателями экстренных оповещений.
   
Команды (пока столько):
1. createEvent — создание нового чрезвычайного события.
2. updateEvent — обновление информации о событии.
3. assignLocation — назначение местоположения для чрезвычайного события.
4. listEvents — вывести все события ЧС.
5. listNotifications — вывести все уведомления.
6. listRecipients — вывести всех получаетелей.

События:
1. EventCreated — событие создано.
2. EventUpdated — информация о событии обновлена.
3. EventLocationAssigned — местоположение события назначено.
4. EventsListed — выведены все события ЧС.
5. NotificationsListed — выведены все уведомления.
6. RecipientsListed — выведены всех получаетелей.

## Инструментарий
Python, VS Code

## Модель данных
На уровне приложения - классы
На уровне хранения - реляционная БД
