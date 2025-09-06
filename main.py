import telebot
from telebot import types
import time
import requests
import random
import json
import os


def load_user_stats():
    if os.path.exists('user_stats.json'):
        with open('user_stats.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def save_user_stats():
    with open('user_stats.json', 'w', encoding='utf-8') as f:
        json.dump(user_stats, f, ensure_ascii=False, indent=2)

bot = telebot.TeleBot('')

quiz_questions = [
    {
        'question': '❓ *Какова основная причина современного глобального потепления?*',
        'options': [
            'Естественные климатические циклы',
            'Деятельность человека',
            'Изменение солнечной активности',
            'Вулканическая активность'
        ],
        'explanation': '✅ *Правильно!* Основная причина - деятельность человека, особенно выбросы парниковых газов от сжигания ископаемого топлива.'
    },
    {
        'question': '🌡️ *На сколько градусов повысилась средняя глобальная температура с конца 19 века?*',
        'options': [
            '0.5°C',
            '1.1°C', 
            '2.0°C',
            '3.5°C'
        ],
        'explanation': '✅ *Верно!* Средняя глобальная температура повысилась на 1.1°C с доиндустриального уровня.'
    },
    {
        'question': '🏭 *Какой сектор является крупнейшим источником парниковых газов?*',
        'options': [
            'Сельское хозяйство',
            'Энергетика',
            'Транспорт',
            'Промышленность'
        ],
        'explanation': '✅ *Правильно!* Энергетический сектор (производство электроэнергии и тепла) - крупнейший источник выбросов.'
    },
    {
        'question': '🌊 *Что вызывает повышение уровня моря?*',
        'options': [
            'Только таяние ледников',
            'Только тепловое расширение воды',
            'Таяние ледников и тепловое расширение воды',
            'Изменение океанских течений'
        ],
        'explanation': '✅ *Верно!* Повышение уровня моря вызвано как таянием ледников, так и тепловым расширением воды при нагревании.'
    },
    {
        'question': '🌳 *Как леса влияют на климат?*',
        'options': [
            'Усиливают потепление',
            'Поглощают CO₂ из атмосферы',
            'Выделяют парниковые газы',
            'Не влияют на климат'
        ],
        'explanation': '✅ *Правильно!* Леса действуют как углеродные sinks, поглощая CO₂ из атмосферы через фотосинтез.'
    },
    {
        'question': '🔥 *Что такое парниковый эффект?*',
        'options': [
            'Охлаждение атмосферы',
            'Удержание тепла в атмосферы',
            'Увеличение кислорода',
            'Уменьшение облачности'
        ],
        'explanation': '✅ *Верно!* Парниковый эффект - это удержание тепла в атмосфере Земли парниковыми газами.'
    },
    {
        'question': '🌪️ *Какое из этих явлений УЧАЩАЕТСЯ из-за изменения климата?*',
        'options': [
            'Зимние морозы',
            'Экстремальные засухи',
            'Вулканические извержения',
            'Землетрясения'
        ],
        'explanation': '✅ *Правильно!* Экстремальные засухи и волны жары учащаются из-за глобального потепления.'
    },
    {
        'question': '🐋 *Как изменение климата влияет на океаны?*',
        'options': [
            'Повышение кислотности',
            'Понижение уровня',
            'Увеличение солености',
            'Уменьшение температуры'
        ],
        'explanation': '✅ *Верно!* Океаны поглощают CO₂, что приводит к их подкислению, вредному для морской жизни.'
    },
    {
        'question': '🌍 *Что такое Парижское соглашение?*',
        'options': [
            'Торговый договор',
            'Соглашение о защите климата',
            'Военный альянс',
            'Культурный обмен'
        ],
        'explanation': '✅ *Правильно!* Парижское соглашение - международный договор по ограничению глобального потепления.'
    },
    {
        'question': '💨 *Какой газ является основным парниковым газом?*',
        'options': [
            'Кислород (O₂)',
            'Азот (N₂)',
            'Углекислый газ (CO₂)',
            'Водород (H₂)'
        ],
        'explanation': '✅ *Верно!* CO₂ - основной парниковый газ, contributing около 76% к парниковому эффекту.'
    },
    {
        'question': '🔄 *Что означает "углеродный нейтралитет"?*',
        'options': [
            'Полное отсутствие выбросов',
            'Баланс выбросов и поглощения CO₂',
            'Использование только угля',
            'Запрет на все производства'
        ],
        'explanation': '✅ *Правильно!* Углеродный нейтралитет - баланс между выбросами углерода и его поглощением из атмосферы.'
    }
]


user_stats = load_user_stats()

climate_facts = [
    "🌍 *Факт:* Последнее десятилетие (2011-2020) было самым теплым в истории наблюдений!",
    "🔥 *Факт:* Концентрация CO₂ в атмосфере самая высокая за последние 2 миллиона лет!",
    "🌪️ *Факт:* Экстремальные погодные явления участились на 50% за последние 20 лет!",
    "🐼 *Факт:* 1 миллион видов животных и растений находится под угрозой исчезновения из-за изменения климата!",
    "🌊 *Факт:* Уровень моря поднимается на 3.6 мм в год - это в 2.5 раза быстрее, чем в 20 веке!"
]

eco_tips = [
    "💡 *Совет:* Замените лампы накаливания на светодиодные - экономия до 80% энергии!",
    "🚲 *Совет:* Проезжая 10 км на велосипеде вместо машины, вы предотвращаете выброс 2 кг CO₂!",
    "🥦 *Совет:* Один день без мяса в неделю = экономия 700 кг CO₂ в год на человека!",
    "🚰 *Совет:* Выключайте воду при чистке зубов - экономия 10 литров воды в минуту!",
    "🛍️ *Совет:* Используйте многоразовую сумку вместо пластиковых пакетов - каждый пакет разлагается 400 лет!"
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = str(message.from_user.id)
    if user_id not in user_stats:
        user_stats[user_id] = {
            'quizzes_taken': 0,
            'level': 'Новичок'
        }
    
    save_user_stats()
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton("❓ Информация", callback_data='info'),
        types.InlineKeyboardButton("🔍 Причины", callback_data='causes'),
        types.InlineKeyboardButton("⚠️ Последствия", callback_data='effects'),
        types.InlineKeyboardButton("💡 Решения", callback_data='solutions'),
        types.InlineKeyboardButton("🌱 Советы", callback_data='tips'),
        types.InlineKeyboardButton("🎯 Квиз", callback_data='quiz'),
        types.InlineKeyboardButton("📊 Статистика", callback_data='stats'),
        types.InlineKeyboardButton("🌍 Факт", callback_data='fact')
    ]
    markup.add(*buttons)
    
    welcome_text = f"""
🌍 *Добро пожаловать в ClimateBot, {message.from_user.first_name}!* 🌍

Выберите действие ниже 👇
    """
    bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ['info', 'causes', 'effects', 'solutions', 'tips', 'quiz', 'stats', 'fact', 'back_to_main'])
def handle_main_callbacks(call):
    try:
        if call.data == 'info':
            send_info(call.message)
        elif call.data == 'causes':
            send_causes(call.message)
        elif call.data == 'effects':
            send_effects(call.message)
        elif call.data == 'solutions':
            send_solutions(call.message)
        elif call.data == 'tips':
            send_random_tip(call.message)
        elif call.data == 'quiz':
            start_quiz(call.message)
        elif call.data == 'stats':
            show_stats(call.message)
        elif call.data == 'fact':
            send_random_fact(call.message)
        elif call.data == 'back_to_main':
            send_welcome(call.message)
        
        bot.answer_callback_query(call.id)
    except Exception as e:
        print(f"Ошибка в обработке callback: {e}")
        try:
            bot.answer_callback_query(call.id)
        except:
            pass

@bot.callback_query_handler(func=lambda call: call.data.startswith('answer_'))
def handle_quiz_answer(call):
    try:
        user_id = str(call.from_user.id)
        if user_id not in user_stats or 'current_question' not in user_stats[user_id]:
            bot.answer_callback_query(call.id, "Начните новый квиз! /quiz")
            return
            
        current_q = user_stats[user_id]['current_question']
        

        if current_q >= len(quiz_questions):
            bot.answer_callback_query(call.id, "Квиз уже завершен! Начните новый.")
            return
            
        question_data = quiz_questions[current_q]
        explanation = question_data['explanation']
        
        bot.send_message(call.message.chat.id, explanation, parse_mode='Markdown')
        

        user_stats[user_id]['current_question'] += 1
        
        save_user_stats()
        
        time.sleep(1)
        

        if user_stats[user_id]['current_question'] < len(quiz_questions):
            ask_question(call.message)
        else:
            finish_quiz(call.message)
        
    except Exception as e:
        print(f"Ошибка в обработке ответа: {e}")
        try:
            bot.answer_callback_query(call.id)
        except:
            pass

@bot.message_handler(commands=['info'])
def send_info(message):
    info_text = """
*❓ Что такое глобальное потепление?*

Глобальное потепление — это долгосрочное повышение *средней температуры климатической системы Земли*, наблюдаемое уже более века.

📊 *Ключевые факты:*
• +1.1°C - повышение температуры с доиндустриального уровня
• 2011-2020 - самое теплое десятилетие в истории
• 4 - каждое последнее десятилетие было теплее предыдущего

🌡️ *Это компонент антропогенного изменения климата*, вызванного деятельностью человека.
    """
    bot.send_message(message.chat.id, info_text, parse_mode='Markdown')

@bot.message_handler(commands=['causes'])
def send_causes(message):
    causes_text = """
*🔍 Основные причины глобального потепления:*

1. *Энергетика* (75% выбросов) 
   • Сжигание угля, нефти, газа
   • Производство электроэнергии

2. *Транспорт* (15% выбросов)
   • Автомобили, самолеты, корабли
   • Дизельное и бензиновое топливо

3. *Сельское хозяйство* (10% выбросов)
   • Метан от животноводства
   • Удобрения с закисью азота

4. *Промышленность* 
   • Производство цемента, стали
   • Химические процессы

5. *Вырубка лесов*
   • Потеря 12 млн гектаров леса ежегодно
   • Снижение способности поглощать CO₂
    """
    bot.send_message(message.chat.id, causes_text, parse_mode='Markdown')

@bot.message_handler(commands=['effects'])
def send_effects(message):
    effects_text = """
*⚠️ Последствия глобального потепления:*

🌪️ *Экстремальные явления:*
• Учащение волн жары и засух
• Усиление ураганов и наводнений
• Непредсказуемые погодные условия

🌊 *Повышение уровня моря:*
• +3.6 мм в год - текущая скорость
• Угроза прибрежным городам
• Затопление островных государств

🐼 *Воздействие на природу:*
• Исчезновение 1 млн видов
• Подкисление океанов
• Таяние вечной мерзлоты

👥 *Влияние на людей:*
• Риск для продовольственной безопасности
• Ухудшение здоровья населения
• Вынужденная миграция миллионов
    """
    bot.send_message(message.chat.id, effects_text, parse_mode='Markdown')

@bot.message_handler(commands=['solutions'])
def send_solutions(message):
    solutions_text = """
*💡 Решения для борьбы с изменением климата:*

🌞 *Энергетический переход:*
• Солнечная и ветровая энергия
• Электромобили и ВИЭ
• Энергоэффективные технологии

🌳 *Природные решения:*
• Восстановление лесов
• Защита экосистем
• Устойчивое сельское хозяйство

🏭 *Промышленные инновации:*
• Улавливание CO₂
• Зеленая сталь и цемент
• Циркулярная экономика

🤝 *Международное сотрудничество:*
• Парижское соглашение
• Цель: нулевые выбросы к 2050
• Глобальное финансирование

*Каждый может внести вклад!* 🌍
    """
    bot.send_message(message.chat.id, solutions_text, parse_mode='Markdown')

@bot.message_handler(commands=['tips'])
def send_random_tip(message):
    tip = random.choice(eco_tips)
    bot.send_message(message.chat.id, tip, parse_mode='Markdown')

@bot.message_handler(commands=['fact'])
def send_random_fact(message):
    fact = random.choice(climate_facts)
    bot.send_message(message.chat.id, fact, parse_mode='Markdown')

@bot.message_handler(commands=['stats'])
def show_stats(message):
    user_id = str(message.from_user.id)
    if user_id in user_stats:
        stats = user_stats[user_id]
        
        stats_text = f"""
📊 *Ваша статистика, {message.from_user.first_name}:*

📝 Пройдено квизов: {stats['quizzes_taken']}
🎯 Уровень: {stats['level']}
        """
    else:
        stats_text = "📊 Вы еще не начали! Нажмите /start чтобы начать."
    
    bot.send_message(message.chat.id, stats_text, parse_mode='Markdown')

@bot.message_handler(commands=['quiz'])
def start_quiz(message):
    user_id = str(message.from_user.id)
    if user_id not in user_stats:
        user_stats[user_id] = {
            'quizzes_taken': 0,
            'level': 'Новичок'
        }
    
    user_stats[user_id]['current_question'] = 0
    user_stats[user_id]['quizzes_taken'] += 1
    
    save_user_stats()
    
    ask_question(message)

def ask_question(message):
    user_id = str(message.from_user.id)
    current_q = user_stats[user_id].get('current_question', 0)
    
    if current_q < len(quiz_questions):
        question_data = quiz_questions[current_q]
        
        markup = types.InlineKeyboardMarkup(row_width=2)
        buttons = []
        for i, option in enumerate(question_data['options']):
            buttons.append(types.InlineKeyboardButton(option, callback_data=f'answer_{i}'))
        markup.add(*buttons)
        
        if 'last_quiz_message_id' in user_stats[user_id]:
            try:
                bot.delete_message(message.chat.id, user_stats[user_id]['last_quiz_message_id'])
            except:
                pass
        
        sent_message = bot.send_message(message.chat.id, question_data['question'], parse_mode='Markdown', reply_markup=markup)
        user_stats[user_id]['last_quiz_message_id'] = sent_message.message_id
        
    else:
        finish_quiz(message)

def finish_quiz(message):
    user_id = str(message.from_user.id)
    
    result_text = f"""
🎉 *Квиз завершен!*

Вы ответили на все {len(quiz_questions)} вопросов о изменении климата!

Надеемся, вы узнали что-то новое о нашей планете 🌍
    """
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🎯 Еще квиз", callback_data='quiz'))
    markup.add(types.InlineKeyboardButton("📊 Статистика", callback_data='stats'))
    
    bot.send_message(message.chat.id, result_text, parse_mode='Markdown', reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()
    
    if text in ['привет', 'hello', 'hi', 'начать']:
        bot.reply_to(message, f"Привет, {message.from_user.first_name}! 🌍 Используйте /start для меню.")
    elif text in ['спасибо', 'благодарю', 'thanks']:
        bot.reply_to(message, "Всегда рад помочь! 🌱")
    elif text in ['помощь', 'help', 'команды']:
        bot.reply_to(message, "Используйте /start для главного меню или:\n/info - информация\n/quiz - квиз\n/tips - советы\n/fact - факты\n/stats - статистика")
    else:
        bot.reply_to(message, "Извините, я не понимаю. Используйте /start для просмотра команд.")

def check_internet_connection():
    try:
        requests.get('https://api.telegram.org', timeout=5)
        return True
    except:
        return False

if __name__ == '__main__':
    print("🌍 ClimateBot запускается...")
    
    while True:
        try:
            if check_internet_connection():
                print("✅ Соединение установлено. Бот активен!")
                bot.polling(none_stop=True, interval=1, timeout=60)
            else:
                print("❌ Нет интернет-соединения. Повторная попытка через 15 секунд...")
                time.sleep(15)
        except Exception as e:
            print(f"⚠️ Ошибка: {e}. Перезапуск через 15 секунд...")
            time.sleep(15)
